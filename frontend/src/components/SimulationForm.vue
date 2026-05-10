<template>
  <Panel title="Параметры модели">
    <template #icon>
      <IconGear/>
    </template>
    <Accordion title="Начальные условия">
      <template #icon>
        <IconTable/>
      </template>
      <div class="param-group">
        <NumberInput
            label="T0 (CD4+)"
            v-model="localParams.initials.T"
            :step="10"
            :min="0"
            :max="2000"
            unit="кл/мкл"
            required
        />
        <NumberInput
            label="L0 (латентные)"
            v-model="localParams.initials.L"
            :step="1"
            :min="0"
            unit="кл/мкл"
            required
        />
        <NumberInput
            label="I0 (продуктивные)"
            v-model="localParams.initials.I"
            :step="0.1"
            :min="0"
            unit="кл/мкл"
            required
        />
        <NumberInput
            label="V0 (вирус)"
            v-model="localParams.initials.V"
            :step="10"
            :min="0"
            unit="копий/мл"
            required
        />
        <NumberInput
            label="C0 (CTL)"
            v-model="localParams.initials.C"
            :step="10"
            :min="0"
            unit="кл/мкл"
            required
        />
      </div>
    </Accordion>

    <Accordion title="Биологические параметры">
      <template #icon>
        <IconCells/>
      </template>
      <div class="param-group">
        <NumberInput
            label="λ (приток CD4+)"
            v-model="localParams.biological.lambda"
            :step="1"
            :min="0"
            clue="5 – 15"
            required
        />

        <NumberInput
            label="r (пролиферация)"
            v-model="localParams.biological.r"
            :step="0.01"
            :min="0"
            :max="1"
            clue="0.05 – 0.2"
            required
        />

        <NumberInput
            label="T_max (емкость)"
            v-model="localParams.biological.T_max"
            :step="100"
            :min="0"
            clue="500 – 2000"
            required
        />

        <NumberInput
            label="d_T (гибель CD4+)"
            v-model="localParams.biological.d_T"
            :step="0.001"
            :min="0"
            clue="10⁻⁶ – 10⁻²"
            required
        />

        <NumberInput
            label="β (скорость заражения)"
            v-model="localParams.biological.beta"
            :step="1e-8"
            :min="0"
            clue="10⁻⁸ – 10⁻⁶"
            required
        />

        <NumberInput
            label="ρ (доля латентных)"
            v-model="localParams.biological.rho"
            :step="0.01"
            :min="0"
            :max="1"
            clue="10⁻⁶ – 10⁻¹"
            required
        />

        <NumberInput
            label="a (реактивация)"
            v-model="localParams.biological.a"
            :step="0.001"
            :min="0"
            clue="10⁻⁴ – 10⁻²"
            required
        />

        <NumberInput
            label="δ_L (гибель латентных)"
            v-model="localParams.biological.delta_L"
            :step="0.001"
            :min="0"
            clue="10⁻⁴ – 10⁻²"
            required
        />

        <NumberInput
            label="δ_I (гибель продуктивных)"
            v-model="localParams.biological.delta_I"
            :step="0.1"
            :min="0"
            clue="0.3 – 1.0"
            required
        />

        <NumberInput
            label="κ (уничтожение CTL)"
            v-model="localParams.biological.kappa"
            :step="0.01"
            :min="0"
            clue="10⁻⁶ – 10⁻⁴"
            required
        />
      </div>
    </Accordion>

    <Accordion title="Вирус и иммунитет">
      <template #icon>
        <IconVirus/>
      </template>
      <div class="param-group">
        <NumberInput
            label="p (продукция вируса)"
            v-model="localParams.virus.p"
            :step="10"
            :min="0"
            clue="50 – 1000"
            required
        />

        <NumberInput
            label="c (клиренс вируса)"
            v-model="localParams.virus.c"
            :step="1"
            :min="0"
            clue="1 – 5"
            required
        />

        <NumberInput
            label="φ (нейтрализация CTL)"
            v-model="localParams.virus.phi"
            :step="0.001"
            :min="0"
            clue="10⁻⁶ – 10⁻⁴"
            required
        />

        <NumberInput
            label="s_C (приток CTL)"
            v-model="localParams.immune.s_C"
            :step="0.1"
            :min="0"
            clue="0.1 – 2"
            required
        />

        <NumberInput
            label="α (активация CTL)"
            v-model="localParams.immune.alpha"
            :step="0.01"
            :min="0"
            clue="0.1 – 10"
            required
        />

        <NumberInput
            label="h (насыщение)"
            v-model="localParams.immune.h"
            :step="50"
            :min="0"
            clue="1 – 50"
            required
        />

        <NumberInput
            label="d_C (гибель CTL)"
            v-model="localParams.immune.d_C"
            :step="0.01"
            :min="0"
            clue="0.05 – 0.2"
            required
        />

        <NumberInput
            label="η_C (истощение)"
            v-model="localParams.immune.eta_C"
            :step="0.01"
            :min="0"
            clue="10⁻³ – 10⁻¹"
            required
        />

        <NumberInput
            label="q (порог)"
            v-model="localParams.immune.q"
            :step="50"
            :min="0"
            clue="1 – 50"
            required
        />
      </div>
    </Accordion>

    <Accordion title="Антиретровирусная терапия">
      <template #icon>
        <IconCapsule/>
      </template>
      <div class="param-group">
        <SelectInput
            label="Режим ε_inf"
            v-model="localParams.therapy.mode_inf"
            :options="therapyOptions"
            required
        />
        <NumberInput
            label="ε0_inf"
            v-model="localParams.therapy.epsilon0_inf"
            :step="0.05"
            :min="0"
            :max="1"
            :disabled="localParams.therapy.mode_inf === 'WITHOUT'"
            required
        />
        <NumberInput
            :label="gammaInf_label"
            v-model="localParams.therapy.gamma_inf"
            :step="gammaInf_step"
            :min="0"
            :disabled="localParams.therapy.mode_inf === 'WITHOUT'"
            required
        />

        <hr/>

        <SelectInput
            label="Режим ε_prod"
            v-model="localParams.therapy.mode_prod"
            :options="therapyOptions"
            required
        />
        <NumberInput
            label="ε0_prod"
            v-model="localParams.therapy.epsilon0_prod"
            :step="0.05"
            :min="0"
            :max="1"
            :disabled="localParams.therapy.mode_prod === 'WITHOUT'"
            required
        />
        <NumberInput
            :label="gammaProd_label"
            v-model="localParams.therapy.gamma_prod"
            :step="gammaProd_step"
            :min="0"
            :disabled="localParams.therapy.mode_prod === 'WITHOUT'"
            required
        />
      </div>
    </Accordion>

    <Accordion title="Время симуляции">
      <template #icon>
        <IconTime/>
      </template>
      <div class="param-group">
        <NumberInput
            label="T_max (дней)"
            v-model="localParams.sim.t_max"
            :step="50"
            :min="1"
            required
        />
        <SliderInput
            label="Количество точек"
            v-model="localParams.sim.num_points"
            :min="1000"
            :max="100000"
            ::step="100"
            required
        />
      </div>
    </Accordion>

    <Button
        type="submit"
        @click="simulationRun"
        :disabled="isDisabled"
        custom-class="submit__btn"
    >
      <template #icon>
        <IconLaboratory/>
      </template>
      ЗАПУСТИТЬ
    </Button>

    <ProgressBar :loading="loading"/>

    <Button
        v-if="loading"
        type="button"
        @click="simulationAbort"
        custom-class="abort__btn"
    >
      <template #icon>
        <IconStop/>
      </template>
      Остановить расчет
    </Button>
  </Panel>
</template>

<script setup>
import {computed, reactive} from 'vue'
import IconTime from "@/components/icons/IconTime.vue";
import IconCells from "@/components/icons/IconCells.vue";
import IconVirus from "@/components/icons/IconVirus.vue";
import IconCapsule from "@/components/icons/IconCapsule.vue";
import IconTable from "@/components/icons/IconTable.vue";
import IconGear from "@/components/icons/IconGear.vue";
import IconLaboratory from "@/components/icons/IconLaboratory.vue";

import Accordion from "@/components/ui/Accordion.vue";
import Button from "@/components/ui/Button.vue";
import SliderInput from "@/components/ui/SliderInput.vue";
import NumberInput from "@/components/ui/NumberInput.vue";
import SelectInput from "@/components/ui/SelectInput.vue";
import Panel from "@/components/ui/Panel.vue";
import IconStop from "@/components/icons/IconStop.vue";

import {getGammaLabel, getGammaStep} from '@/utils/gammaHelpers'
import ProgressBar from "@/components/ui/ProgressBar.vue";

const props = defineProps({
  loading: Boolean
})

const isDisabled = computed(() => {
  return props.loading
})

const defaultParams = reactive({
  initials: {T: 1000, L: 0, I: 0, V: 1000, C: 500},
  biological: {
    lambda: 10, r: 0.1, T_max: 1600, d_T: 0.005, beta: 0.00001,
    rho: 0.00001, a: 0.001, delta_L: 0.001, delta_I: 0.5, kappa: 0.00001
  },
  virus: {p: 500, c: 3, phi: 0.00001},
  immune: {s_C: 2, alpha: 10, h: 50, d_C: 0.1, eta_C: 0.01, q: 50},
  therapy: {
    mode_inf: 'WITHOUT', epsilon0_inf: 0.9, gamma_inf: 0.01,
    mode_prod: 'WITHOUT', epsilon0_prod: 0.8, gamma_prod: 0.01
  },
  sim: {t_max: 350, num_points: 3500}
})
const localParams = reactive(defaultParams)

const therapyOptions = [
  {value: 'WITHOUT', label: 'Без терапии'},
  {value: 'THERAPY', label: 'Включение на n-ый день'},
  {value: 'INTERRUPTION', label: 'Прием с периодичностью γ'},
  {value: 'RESISTANCE', label: 'Развитие резистентности'}
]

const emit = defineEmits(['run', 'abort'])

function simulationRun() {
  emit('run', localParams)
}

function simulationAbort() {
  emit('abort')
}

const gammaInf_label = computed(() => getGammaLabel(localParams.therapy.mode_inf))
const gammaInf_step = computed(() => getGammaStep(localParams.therapy.mode_inf))

const gammaProd_label = computed(() => getGammaLabel(localParams.therapy.mode_prod))
const gammaProd_step = computed(() => getGammaStep(localParams.therapy.mode_prod))

</script>