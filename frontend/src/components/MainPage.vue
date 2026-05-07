<template>
  <div class="app-container">

    <aside class="sidebar">
      <SimulationForm />
    </aside>

    <main class="content">
      <ModelDescription />
      <hr />
      <ResultsDisplay />
    </main>
  </div>
</template>

<script setup>
import SimulationForm from "@/components/SimulationForm.vue";
import ModelDescription from "@/components/ModelDescription.vue";
import ResultsDisplay from "@/components/ResultsDisplay.vue";
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
  padding: 1rem;
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