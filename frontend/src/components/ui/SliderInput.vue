<template>
  <div class="slider-wrapper">
    <div class="slider-header">
      <label v-if="label">{{ label }}</label>
      <NumberInput
          :modelValue="modelValue"
          @update:modelValue="$emit('update:modelValue', $event)"
          :step="step"
          :min="min"
          :max="max"
          :unit="unit"
      />
    </div>
    <input
        type="range"
        :value="modelValue"
        @input="$emit('update:modelValue', parseFloat($event.target.value))"
        :min="min"
        :max="max"
        :step="step"
        class="slider"
    />
  </div>
</template>

<script setup>
import NumberInput from './NumberInput.vue'

defineProps({
  modelValue: Number,
  label: String,
  min: { type: Number, default: 0 },
  max: { type: Number, default: 100 },
  step: { type: Number, default: 1 },
  unit: String
})

defineEmits(['update:modelValue'])
</script>

<style scoped>
.slider-wrapper {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 12px;
}
.slider-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}
.slider-header label {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-secondary, #475569);
}
.slider {
  width: 100%;
  height: 4px;
  border-radius: 2px;
  background: var(--border-color, #e2e8f0);
  accent-color: var(--color-primary, #2563eb);
}
</style>