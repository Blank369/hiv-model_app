<template>
  <div class="select-wrapper">
    <label v-if="label">{{ label }}</label>
    <select :value="modelValue" @change="$emit('update:modelValue', $event.target.value)">
      <option v-for="opt in options" :key="opt.value" :value="opt.value">
        {{ opt.label }}
      </option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  modelValue: String,
  label: String,
  options: {
    type: Array,
    required: true,
    validator: (arr) => arr.every(opt => 'value' in opt && 'label' in opt)
  }
})

defineEmits(['update:modelValue'])
</script>

<style scoped>
.select-wrapper {
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
select {
  padding: 6px 10px;
  border: 1px solid var(--border-light, #e2e8f0);
  border-radius: var(--radius-sm, 6px);
  background: white;
  font-family: inherit;
  font-size: 0.9rem;
  cursor: pointer;
}
select:focus {
  outline: none;
  border-color: var(--color-primary, #2563eb);
}
</style>