<template>
  <button
      :class="customClass"
      :type="type"
      :disabled="disabled">
    <slot/>
    <slot name="icon"></slot>
  </button>
</template>

<script setup>
defineProps({
  type: { type: String, default: 'button' },
  disabled: {type: Boolean, default: false },
  customClass: { type: String, default: '' }
})
</script>

<style scoped>
button{
  padding: 12px;
  width: 100%;
  border: none;
  background-color: var(--color-primary);
  border-radius: var(--radius-lg);
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  margin-top: 2rem;
  transition: all 0.2s;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
button:hover{
  transform: scale(1.01);
}
button:disabled{
  background-color: var(--accent-disabled);
  transform: none;
}

.submit__btn {
  background-color: var(--accent-main);
  color: var(--text-light);
}
.submit__btn:hover {
  background-color: var(--accent-hover);
}

.abort__btn {
  margin-top: 1rem;
  background-color: var(--accent-danger);
  color: var(--text-light);
}
.abort__btn:hover {
  background-color: var(--accent-danger-hover);
}

</style>