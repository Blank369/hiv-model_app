<template>
  <BigContainer title="Результаты моделирования">
    <template #icon>
      <IconGraph/>
    </template>

    <Accordion title="📈 Динамика всех переменных">
      <div class="plot-container">
        <LineChart :data="allVariablesChart" :options="chartOptions" />
      </div>
    </Accordion>

    <Accordion title="🔬 Графики переменных" :isOpen="false">
      <div class="plots-grid">
        <div class="single-plot">
          <h4>CD4⁺-лимфоциты (T)</h4>
          <LineChart :data="tCellChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Вирусная нагрузка (V)</h4>
          <LineChart :data="virusChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Латентный резервуар (L)</h4>
          <LineChart :data="latentChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Продуктивные клетки (I)</h4>
          <LineChart :data="infectedChart" :options="simpleOptions" />
        </div>
        <div class="single-plot">
          <h4>Эффекторные клетки (C)</h4>
          <LineChart :data="ctlChart" :options="simpleOptions" />
        </div>
      </div>
    </Accordion>

    <Accordion
        v-if="hasTherapy"
        title="💊 Эффективность терапии"
        :isOpen="false"
    >
      <div class="plot-container">
        <LineChart :data="therapyChart" :options="therapyOptions" />
      </div>
    </Accordion>
  </BigContainer>
</template>

<script setup>
import { computed } from 'vue'
import Accordion from "@/components/ui/Accordion.vue";
import LineChart from "@/components/ui/LineChart.vue";
import BigContainer from "@/components/ui/BigContainer.vue";
import IconGraph from "@/components/icons/IconGraph.vue";

const props = defineProps({
  results: {
    type: Object,
    default: null
  },
  therapyEps: {
    type: Object,
    default: null
  }
})

const hasTherapy = computed(() => {
  return props.therapyEps && props.therapyEps.eps_inf?.some(v => v > 0)
})

// Основной график: все переменные
const allVariablesChart = computed(() => {
  if (!props.results) return { labels: [], datasets: [] }

  const colors = {
    T: '#2563eb',
    L: '#eab308',
    I: '#f97316',
    C: '#22c55e'
  }

  return {
    labels: props.results.t,
    datasets: [
      {
        label: 'T (CD4⁺)',
        data: props.results.T,
        borderColor: colors.T,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      },
      {
        label: 'L (латентные)',
        data: props.results.L,
        borderColor: colors.L,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 1.5,
        borderDash: [5, 5]
      },
      {
        label: 'I (продуктивные)',
        data: props.results.I,
        borderColor: colors.I,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 1.5,
        borderDash: [3, 3]
      },
      {
        label: 'C (CTL)',
        data: props.results.C,
        borderColor: colors.C,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      }
    ]
  }
})

// Отдельные графики
const tCellChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'CD4⁺ (кл/мкл)',
    data: props.results?.T || [],
    borderColor: '#2563eb',
    backgroundColor: 'rgba(37, 99, 235, 0.1)',
    fill: true,
    tension: 0.3
  }]
}))

const virusChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'Вирус (копий/мл)',
    data: props.results?.V || [],
    borderColor: '#ef4444',
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const ctlChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'CTL (кл/мкл)',
    data: props.results?.C || [],
    borderColor: '#22c55e',
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const latentChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'Латентные (кл/мкл)',
    data: props.results?.L || [],
    borderColor: '#eab308',
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

const infectedChart = computed(() => ({
  labels: props.results?.t || [],
  datasets: [{
    label: 'Продуктивные (кл/мкл)',
    data: props.results?.I || [],
    borderColor: '#f97316',
    backgroundColor: 'transparent',
    tension: 0.3
  }]
}))

// Терапия
const therapyChart = computed(() => {
  if (!props.therapyEps || !props.results) return { labels: [], datasets: [] }

  return {
    labels: props.results.t,
    datasets: [
      {
        label: 'ε_inf',
        data: props.therapyEps.eps_inf,
        borderColor: '#2563eb',
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      },
      {
        label: 'ε_prod',
        data: props.therapyEps.eps_prod,
        borderColor: '#f97316',
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