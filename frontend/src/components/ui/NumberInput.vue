<template>
  <div class="input-wrapper" :class="{ 'has-error': error }">
    <label v-if="label">{{ label }}</label>
    <div class="input-container">
      <input
          type="number"
          :value="modelValue"
          @input="updateValue($event.target.value)"
          :step="step"
          :min="min"
          :max="max"
          :disabled="disabled"
          :placeholder="placeholder"
      />
      <span v-if="unit" class="unit">{{ unit }}</span>
    </div>
    <span v-if="error" class="error-message">{{ error }}</span>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: [Number, String],
  label: String,
  step: { type: Number, default: 1 },
  min: { type: Number, default: -Infinity },
  max: { type: Number, default: Infinity },
  unit: String,
  disabled: Boolean,
  placeholder: String,
  required: Boolean
})

const emit = defineEmits(['update:modelValue'])

const error = computed(() => {
  const val = parseFloat(props.modelValue)
  if (isNaN(val) && props.required) return 'Поле обязательно'
  if (val < props.min) return `Минимум ${props.min}`
  if (val > props.max) return `Максимум ${props.max}`
  return null
})

function updateValue(value) {
  if (value === '') {
    emit('update:modelValue', null)
    return
  }
  const num = parseFloat(value)
  if (!isNaN(num)) {
    let clamped = Math.min(Math.max(num, props.min), props.max)
    emit('update:modelValue', clamped)
  } else {
    emit('update:modelValue', value)
  }
}
</script>

<style scoped>
.input-wrapper {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 8px;
}
label {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-secondary, #475569);
}
.input-container {
  display: flex;
  align-items: center;
  gap: 8px;
}
input {
  flex: 1;
  padding: 6px 10px;
  border: 1px solid var(--border-color, #e2e8f0);
  border-radius: var(--radius-sm, 6px);
  font-family: inherit;
  font-size: 0.9rem;
  transition: all 0.2s;
}
input:focus {
  outline: none;
  border-color: var(--color-primary, #2563eb);
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.1);
}
.unit {
  font-size: 0.8rem;
  color: var(--text-secondary, #94a3b8);
  min-width: 50px;
}
.error-message {
  font-size: 0.75rem;
  color: var(--accent-danger, #ef4444);
}
.has-error input {
  border-color: var(--accent-danger, #ef4444);
}
</style>