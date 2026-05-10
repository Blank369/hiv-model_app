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
          <LineChart :data="TChart" :options="cellChartOptions" />
        </div>
        <div class="single-plot">
          <h4>Вирусная нагрузка (V)</h4>
          <LineChart :data="VChart" :options="virusChartOptions" />
        </div>
        <div class="single-plot">
          <h4>Латентный резервуар (L)</h4>
          <LineChart :data="LChart" :options="cellChartOptions" />
        </div>
        <div class="single-plot">
          <h4>Продуктивные клетки (I)</h4>
          <LineChart :data="IChart" :options="cellChartOptions" />
        </div>
        <div class="single-plot">
          <h4>Эффекторные клетки (C)</h4>
          <LineChart :data="CChart" :options="cellChartOptions" />
        </div>
        <div v-if="hasTherapy" class="single-plot">
          <h4>Эффективность терапии</h4>
          <LineChart :data="EChart" :options="therapyChartOptions" />
        </div>
      </div>
    </Accordion>

    <Accordion title="Скачать результаты">
      <template #icon>
        <IconDownload/>
      </template>
      <Button
          type="button"
          class="download__btn"
          @click="$emit('download')"
          :disabled="!isResultsReady"
      >
        <template #icon>
          <IconTxt/>
        </template>
        Скачать в .txt
      </Button>
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
import Button from "@/components/ui/Button.vue";
import IconTxt from "@/components/icons/IconTxt.vue";
import {
  cellChartOptions,
  virusChartOptions,
  therapyChartOptions,
  chartColors,
  createChartData
} from '@/utils/chartHelpers'
import IconDownload from "@/components/icons/IconDownload.vue";


const props = defineProps({
  results: {
    type: Object,
    default: null
  },
  isResultsReady: {
    type: Boolean,
    default: false
  }
})

defineEmits(['download'])

const isOpen = computed(() => {
  return props.results && props.isResultsReady
})

const hasTherapy = computed(() => {
  if (!props.results) return false
  const epsInf = props.results.eps_inf
  const epsProd = props.results.eps_prod
  return (epsInf && epsInf.some(v => v > 0)) || (epsProd && epsProd.some(v => v > 0))
})

const TChart = computed(() => createChartData(props.results?.t, props.results?.T, 'CD4⁺ (кл/мкл)', chartColors.T, { fill: true }))
const LChart = computed(() => createChartData(props.results?.t, props.results?.L, 'Латентные (кл/мкл)', chartColors.L))
const IChart = computed(() => createChartData(props.results?.t, props.results?.I, 'Продуктивные (кл/мкл)', chartColors.I))
const VChart = computed(() => createChartData(props.results?.t, props.results?.V, 'Вирус (копий/мл)', chartColors.V))
const CChart = computed(() => createChartData(props.results?.t, props.results?.C, 'CTL (кл/мкл)', chartColors.C))

const EChart = computed(() => {
  if (!props.results) return { labels: [], datasets: [] }

  return {
    labels: props.results.t,
    datasets: [
      {
        label: 'ε_inf',
        data: props.results.eps_inf || [],
        borderColor: chartColors.eps_inf,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      },
      {
        label: 'ε_prod',
        data: props.results.eps_prod || [],
        borderColor: chartColors.eps_prod,
        backgroundColor: 'transparent',
        tension: 0.3,
        borderWidth: 2
      }
    ]
  }
})


</script>

<style scoped>
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