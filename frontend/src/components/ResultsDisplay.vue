<template>
  <Panel title="Результаты моделирования">
    <template #icon>
      <IconGraph/>
    </template>

    <Accordion title="Графики переменных" :isOpen="isOpen">
      <template #icon>
        <IconChart/>
      </template>
      <div class="plots-grid">
        <div class="single-plot">
          <h4>CD4⁺-лимфоциты (T)</h4>
          <LineChart :data="TChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Вирусная нагрузка (V)</h4>
          <LineChart :data="VChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Латентный резервуар (L)</h4>
          <LineChart :data="LChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Продуктивные клетки (I)</h4>
          <LineChart :data="IChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Эффекторные клетки (C)</h4>
          <LineChart :data="CChart" :options="simpleOptions" />
        </div>
      </div>
    </Accordion>

    <Accordion
        v-if="hasTherapy"
        title="Эффективность терапии"
        :isOpen="false"
    >
      <div class="plot-container">
        <LineChart :data="EChart" :options="therapyOptions" />
      </div>
    </Accordion>
  </Panel>
</template>

<script setup>
import { computed } from 'vue'
import Accordion from "@/components/ui/Accordion.vue";
import LineChart from "@/components/ui/LineChart.vue";
import Panel from "@/components/ui/Panel.vue";
import IconGraph from "@/components/icons/IconGraph.vue";
import IconChart from "@/components/icons/IconChart.vue";
import { chartColors } from '@/assets/css/chartColors.js'

const props = defineProps({
  results: {
    type: Object,
    default: null
  },
  therapyEps: {
    type: Object,
    default: null
  },
  isResultsReady: Boolean
})

const isOpen = computed(() => {
  return props.results && props.isResultsReady
})

const hasTherapy = computed(() => {
  return props.therapyEps && props.therapyEps.eps_inf?.some(v => v > 0)
})

const TChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'CD4⁺ (кл/мкл)',
    data: props.results?.T || [],
    borderColor: chartColors.T,
    backgroundColor: 'transparent',
    fill: true,
    tension: 0.3
  }]
}))

const LChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'Латентные (кл/мкл)',
    data: props.results?.L || [],
    borderColor: chartColors.L,
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const IChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'Продуктивные (кл/мкл)',
    data: props.results?.I || [],
    borderColor: chartColors.I,
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const VChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'Вирус (копий/мл)',
    data: props.results?.V || [],
    borderColor: chartColors.V,
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const CChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'CTL (кл/мкл)',
    data: props.results?.C || [],
    borderColor: chartColors.C,
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const EChart = computed(() => {
  if (!props.therapyEps || !props.results) return { labels: [], datasets: [] }

  return {
    labels: props.results.t,
    datasets: [
      {
        label: 'ε_inf',
        data: props.therapyEps.eps_inf,
        borderColor: chartColors.eps_inf,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      },
      {
        label: 'ε_prod',
        data: props.therapyEps.eps_prod,
        borderColor: chartColors.eps_prod,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      }
    ]
  }
})

// Настройки графиков
const chartOptions = {
  responsive: true,
  maintainAspectRatio: true,
  interaction: { mode: 'index', intersect: false },
  plugins: {
    legend: { position: 'top' },
    tooltip: { mode: 'index', intersect: false }
  }
}

const simpleOptions = {
  responsive: true,
  maintainAspectRatio: true,
  plugins: {
    legend: { position: 'top' }
  }
}

const therapyOptions = {
  responsive: true,
  maintainAspectRatio: true,
  scales: {
    y: { min: 0, max: 1, title: { display: true, text: 'Эффективность ε' } }
  }
}
</script>

<style scoped>
.results-card {
  background: var(--bg-surface);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-color);
  overflow: hidden;
}

.card-header {
  padding: 16px 20px;
  background: var(--bg-hover);
  border-bottom: 1px solid var(--border-color);
}

.card-header h2 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}

.plot-container {
  padding: 16px;
}

.plots-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  padding: 16px;
}

.single-plot {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 12px;
}

.single-plot h4 {
  margin: 0 0 12px 0;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-secondary);
}
</style>