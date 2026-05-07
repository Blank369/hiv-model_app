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
import { onMounted } from 'vue'

const props = defineProps({
  modelValue: String,
  label: String,
  options: {
    type: Array,
    required: true,
    validator: (arr) => arr.every(opt => 'value' in opt && 'label' in opt)
  },
  defaultValue: {
    type: String,
    default: undefined
  }
})

onMounted(() => {
  if (!props.modelValue && props.defaultValue) {
    emit('update:modelValue', props.defaultValue)
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
  color: var(--text-secondary);
}
select {
  padding: 6px 10px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm, 6px);
  background-color: var(--bg-hover);
  font-family: inherit;
  font-size: 0.9rem;
  cursor: pointer;
}
select:focus {
  outline: none;
  border-color: var(--color-primary);
}
</style>