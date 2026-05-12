<template>
  <div class="app-container">

    <aside class="sidebar">
      <SimulationForm @run="handleRun" @abort="handleAbort" :loading="loading" :error-message="errorMessage"/>
    </aside>

    <main class="content">
      <ModelDescription
          :is-results-ready="isReady"
      />
      <hr />
      <ResultsDisplay
          :results="results"
          :is-results-ready="isReady"
          @download="handleDownload"
      />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SimulationForm from "@/components/SimulationForm.vue";
import ModelDescription from "@/components/ModelDescription.vue";
import ResultsDisplay from "@/components/ResultsDisplay.vue";
import { simulationService } from '@/services/SimulationService'

const results = ref(null)
const loading = ref(false)
const errorMessage = ref(null)
const isReady = ref(false)

async function handleRun(formParams) {
  loading.value = true
  errorMessage.value = null
  isReady.value = false

  const payload = {
    initials: formParams.initials,
    biological: formParams.biological,
    virus: formParams.virus,
    immune: formParams.immune,
    therapy: formParams.therapy,
    sim: formParams.sim
  }

  try {
    const response = await simulationService.simulate(payload)
    results.value = response.data
    isReady.value = true
  } catch (error) {
    errorMessage.value = error.error;
  }

  loading.value = false
}

function handleAbort() {
  simulationService.abort()
  loading.value = false
}

async function handleDownload() {
  const response = await simulationService.downloadResult()
  if (!response.success) {
    console.error(response.error)
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app-container {
  display: flex;
  height: 100vh;
  width: 100%;
}
.sidebar {
  width: 360px;
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  overflow-y: auto;
  scrollbar-gutter: stable;
  padding: 1.5rem 0 1.5rem 1rem;

}
.content {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
}
hr {
  margin: 1rem 0;
}

</style>