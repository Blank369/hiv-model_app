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
            label="T0 (CD4⁺)"
            v-model="localParams.initials.T"
            :step="10"
            :min="0"
            :max="2000"
            unit="кл/мкл"
        />
        <NumberInput
            label="L0 (латентные)"
            v-model="localParams.initials.L"
            :step="1"
            :min="0"
            unit="кл/мкл"
        />
        <NumberInput
            label="I0 (продуктивные)"
            v-model="localParams.initials.I"
            :step="0.1"
            :min="0"
            unit="кл/мкл"
        />
        <NumberInput
            label="V0 (вирус)"
            v-model="localParams.initials.V"
            :step="10"
            :min="0"
            unit="копий/мл"
        />
        <NumberInput
            label="C0 (CTL)"
            v-model="localParams.initials.C"
            :step="10"
            :min="0"
            unit="кл/мкл"
        />
      </div>
    </Accordion>

    <Accordion title="Биологические параметры">
      <template #icon>
        <IconCells/>
      </template>
      <div class="param-group">
        <NumberInput
            label="λ (приток CD4⁺)"
            v-model="localParams.biological.lambda"
            :step="1"
            :min="0"
            clue="5 – 15"
        />

        <NumberInput
            label="r (пролиферация)"
            v-model="localParams.biological.r"
            :step="0.01"
            :min="0"
            :max="1"
            clue="0.05 – 0.2"
        />

        <NumberInput
            label="T_max (ёмкость)"
            v-model="localParams.biological.T_max"
            :step="100"
            :min="0"
            clue="500 – 2000"
        />

        <NumberInput
            label="d_T (гибель CD4⁺)"
            v-model="localParams.biological.d_T"
            :step="0.001"
            :min="0"
            clue="10⁻⁶ – 10⁻²"
        />

        <NumberInput
            label="β (скорость заражения)"
            v-model="localParams.biological.beta"
            :step="1e-8"
            :min="0"
            clue="10⁻⁸ – 10⁻⁶"
        />

        <NumberInput
            label="ρ (доля латентных)"
            v-model="localParams.biological.rho"
            :step="0.01"
            :min="0"
            :max="1"
            clue="10⁻⁶ – 10⁻¹"
        />

        <NumberInput
            label="a (реактивация)"
            v-model="localParams.biological.a"
            :step="0.001"
            :min="0"
            clue="10⁻⁴ – 10⁻²"
        />

        <NumberInput
            label="δ_L (гибель латентных)"
            v-model="localParams.biological.delta_L"
            :step="0.001"
            :min="0"
            clue="10⁻⁴ – 10⁻²"
        />

        <NumberInput
            label="δ_I (гибель прод.)"
            v-model="localParams.biological.delta_I"
            :step="0.1"
            :min="0"
            clue="0.3 – 1.0"
        />

        <NumberInput
            label="κ (уничт. CTL)"
            v-model="localParams.biological.kappa"
            :step="0.01"
            :min="0"
            clue="10⁻⁶ – 10⁻⁴"
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
        />

        <NumberInput
            label="c (клиренс вируса)"
            v-model="localParams.virus.c"
            :step="1"
            :min="0"
            clue="1 – 5"
        />

        <NumberInput
            label="φ (нейтрализ. CTL)"
            v-model="localParams.virus.phi"
            :step="0.001"
            :min="0"
            clue="10⁻⁶ – 10⁻⁴"
        />

        <NumberInput
            label="s_C (приток CTL)"
            v-model="localParams.immune.s_C"
            :step="0.1"
            :min="0"
            clue="0.1 – 2"
        />

        <NumberInput
            label="α (активация CTL)"
            v-model="localParams.immune.alpha"
            :step="0.01"
            :min="0"
            clue="0.1 – 10"
        />

        <NumberInput
            label="h (насыщение)"
            v-model="localParams.immune.h"
            :step="50"
            :min="0"
            clue="1 – 50"
        />

        <NumberInput
            label="d_C (гибель CTL)"
            v-model="localParams.immune.d_C"
            :step="0.01"
            :min="0"
            clue="0.05 – 0.2"
        />

        <NumberInput
            label="η_C (истощение)"
            v-model="localParams.immune.eta_C"
            :step="0.01"
            :min="0"
            clue="10⁻³ – 10⁻¹"
        />

        <NumberInput
            label="q (порог)"
            v-model="localParams.immune.q"
            :step="50"
            :min="0"
            clue="1 – 50"
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
        />
        <NumberInput
            label="День начала терапии"
            v-model="localParams.therapy.startday_inf"
            :step="1"
            :min="0"
            unit="день"
        />
        <NumberInput
            label="ε0_inf"
            v-model="localParams.therapy.epsilon0_inf"
            :step="0.05"
            :min="0"
            :max="1"
        />
        <NumberInput
            label="γ_inf"
            v-model="localParams.therapy.gamma_inf"
            :step="0.001"
            :min="0"
        />

        <SelectInput
            label="Режим ε_prod"
            v-model="localParams.therapy.mode_prod"
            :options="therapyOptions"
        />
        <NumberInput
            label="День начала терапии"
            v-model="localParams.therapy.startday_prod"
            :step="1"
            :min="0"
            unit="день"
        />
        <NumberInput
            label="ε0_prod"
            v-model="localParams.therapy.epsilon0_prod"
            :step="0.05"
            :min="0"
            :max="1"
        />
        <NumberInput
            label="γ_prod"
            v-model="localParams.therapy.gamma_prod"
            :step="0.001"
            :min="0"
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
        />
        <SliderInput
            label="Количество точек"
            v-model="localParams.sim.num_points"
            :min="100"
            :max="2000"
            ::step="100"
        />
      </div>
    </Accordion>

    <SubmitButton @click="simulationRun">
      <template #icon>
        <IconLaboratory/>
      </template>
      ЗАПУСТИТЬ
    </SubmitButton>
  </Panel>
</template>

<script setup>
import { reactive } from 'vue'
import IconTime from "@/components/icons/IconTime.vue";
import IconCells from "@/components/icons/IconCells.vue";
import IconVirus from "@/components/icons/IconVirus.vue";
import IconCapsule from "@/components/icons/IconCapsule.vue";
import IconTable from "@/components/icons/IconTable.vue";
import IconGear from "@/components/icons/IconGear.vue";
import IconLaboratory from "@/components/icons/IconLaboratory.vue";

import Accordion from "@/components/ui/Accordion.vue";
import SubmitButton from "@/components/ui/SubmitButton.vue";
import SliderInput from "@/components/ui/SliderInput.vue";
import NumberInput from "@/components/ui/NumberInput.vue";
import SelectInput from "@/components/ui/SelectInput.vue";
import Panel from "@/components/ui/Panel.vue";

const defaultParams = reactive({
  initials: { T: 1000, L: 0, I: 0.1, V: 100, C: 50 },
  biological: {
    lambda: 10, r: 0.1, T_max: 1250, d_T: 0.005, beta: 5e-7,
    rho: 0.05, a: 0.005, delta_L: 0.005, delta_I: 0.65, kappa: 5e-5
  },
  virus: { p: 525, c: 3, phi: 5e-5 },
  immune: { s_C: 1.05, alpha: 5, h: 25, d_C: 0.125, eta_C: 0.05, q: 25 },
  therapy: {
    mode_inf: 'WITHOUT', epsilon0_inf: 0.9, gamma_inf: 0.01, startday_inf: 50,
    mode_prod: 'WITHOUT', epsilon0_prod: 0.8, gamma_prod: 0.01, startday_prod: 50
  },
  sim: { t_max: 500, num_points: 500 }
})
const localParams = reactive(defaultParams)

const therapyOptions = [
  { value: 'WITHOUT', label: 'Без терапии' },
  { value: 'THERAPY', label: 'Включение на n-ый день' },
  { value: 'INTERRUPTION', label: 'Приём с периодичностью γ' },
  { value: 'RESISTANCE ', label: 'Развитие резистентности' }
]

const emit = defineEmits(['run'])

function simulationRun() {
  emit('run', localParams)
}

</script>