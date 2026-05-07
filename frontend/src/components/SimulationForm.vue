<template>
  <div class="params-panel">
    <div class="params__title">
      <IconGear/>
      <h3>Параметры модели</h3>
    </div>

    <Accordion title="Начальные условия" :isOpen="true">
      <template #icon>
        <IconTable/>
      </template>
      <div class="param-group">
        <NumberInput
            label="T0 (CD4⁺)"
            v-model="localParams.initials.T"
            step="10"
            :min="0"
            :max="2000"
            unit="кл/мкл"
        />
        <NumberInput
            label="L0 (латентные)"
            v-model="localParams.initials.L"
            step="1"
            :min="0"
            unit="кл/мкл"
        />
        <NumberInput
            label="I0 (продуктивные)"
            v-model="localParams.initials.I"
            step="0.1"
            :min="0"
            unit="кл/мкл"
        />
        <NumberInput
            label="V0 (вирус)"
            v-model="localParams.initials.V"
            step="10"
            :min="0"
            unit="копий/мл"
        />
        <NumberInput
            label="C0 (CTL)"
            v-model="localParams.initials.C"
            step="10"
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
        <NumberInput label="λ (приток CD4⁺)" v-model="localParams.bio.lambda" step="1" :min="0" />
        <NumberInput label="r (пролиферация)" v-model="localParams.bio.r" step="0.01" :min="0" :max="1" />
        <NumberInput label="T_max (ёмкость)" v-model="localParams.bio.T_max" step="100" :min="0" />
        <NumberInput label="d_T (гибель CD4⁺)" v-model="localParams.bio.d_T" step="0.01" :min="0" />
        <NumberInput label="β (скорость заражения)" v-model="localParams.bio.beta" step="1e-6" :min="0" />
        <NumberInput label="ρ (доля латентных)" v-model="localParams.bio.rho" step="0.05" :min="0" :max="1" />
        <NumberInput label="a (реактивация)" v-model="localParams.bio.a" step="0.01" :min="0" />
        <NumberInput label="δ_L (гибель латентных)" v-model="localParams.bio.delta_L" step="0.001" :min="0" />
        <NumberInput label="δ_I (гибель прод.)" v-model="localParams.bio.delta_I" step="0.5" :min="0" />
        <NumberInput label="κ (уничт. CTL)" v-model="localParams.bio.kappa" step="0.01" :min="0" />
      </div>
    </Accordion>

    <Accordion title="Вирус и иммунитет">
      <template #icon>
        <IconVirus/>
      </template>
      <div class="param-group">
        <NumberInput label="p (продукция вируса)" v-model="localParams.virus.p" step="10" :min="0" />
        <NumberInput label="c (клиренс вируса)" v-model="localParams.virus.c" step="1" :min="0" />
        <NumberInput label="φ (нейтрализ. CTL)" v-model="localParams.virus.phi" step="0.001" :min="0" />
        <NumberInput label="s_C (приток CTL)" v-model="localParams.immune.s_C" step="0.1" :min="0" />
        <NumberInput label="α (активация CTL)" v-model="localParams.immune.alpha" step="0.01" :min="0" />
        <NumberInput label="h (насыщение)" v-model="localParams.immune.h" step="50" :min="0" />
        <NumberInput label="d_C (гибель CTL)" v-model="localParams.immune.d_C" step="0.01" :min="0" />
        <NumberInput label="η_C (истощение)" v-model="localParams.immune.eta_C" step="0.01" :min="0" />
        <NumberInput label="q (порог)" v-model="localParams.immune.q" step="50" :min="0" />
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
            label="ε0_inf"
            v-model="localParams.therapy.epsilon0_inf"
            step="0.05"
            :min="0"
            :max="1"
        />
        <NumberInput
            label="γ_inf"
            v-model="localParams.therapy.gamma_inf"
            step="0.001"
            :min="0"
        />

        <SelectInput
            label="Режим ε_prod"
            v-model="localParams.therapy.mode_prod"
            :options="therapyOptions"
        />
        <NumberInput
            label="ε0_prod"
            v-model="localParams.therapy.epsilon0_prod"
            step="0.05"
            :min="0"
            :max="1"
        />
        <NumberInput
            label="γ_prod"
            v-model="localParams.therapy.gamma_prod"
            step="0.001"
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
            step="50"
            :min="1"
        />
        <SliderInput
            label="Количество точек"
            v-model="localParams.sim.num_points"
            :min="100"
            :max="2000"
            :step="100"
        />
      </div>
    </Accordion>

    <SubmitButton @click="$emit('run', localParams)">
      <template #icon>
        <IconLaboratory/>
      </template>
      ЗАПУСТИТЬ
    </SubmitButton>
  </div>
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

const defaultParams = {
  initials: { T: 1000, L: 0, I: 0.1, V: 100, C: 50 },
  bio: {
    lambda: 10, r: 0.03, T_max: 1500, d_T: 0.01, beta: 2.4e-5,
    rho: 0.1, a: 0.01, delta_L: 0.001, delta_I: 1.0, kappa: 0.01
  },
  virus: { p: 100, c: 10, phi: 0.001 },
  immune: { s_C: 0.1, alpha: 0.1, h: 100, d_C: 0.01, eta_C: 0.01, q: 100 },
  therapy: { mode_inf: 'step', epsilon0_inf: 0.9, gamma_inf: 0.01, mode_prod: 'step', epsilon0_prod: 0.8, gamma_prod: 0.01 },
  sim: { t_max: 500, num_points: 0.001 }
}

const therapyOptions = [
  { value: 'WITHOUT', label: 'Без терапии' },
  { value: 'THERAPY', label: 'Включение на n-ый день' },
  { value: 'INTERRUPTION', label: 'Приём с периодичностью γ' },
  { value: 'RESISTANCE ', label: 'Развитие резистентности' }
]

const localParams = reactive(defaultParams)

</script>

<style scoped>
.params-panel {
  display: flex;
  flex-direction: column;
  gap: 8px;
  background-color: var(--bg-sidebar);
}
.params__title{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-right: 10px;
}

h3 {
  margin-bottom: 12px;
  padding-left: 6px;
}
.param-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.param-group label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  font-size: 0.9rem;
}
.param-grid label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  gap: 8px;
}
input, select {
  padding: 4px 8px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-family: inherit;
  width: 120px;
}

</style>