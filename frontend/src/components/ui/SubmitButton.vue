<script setup>

</script>

<template>
  <button class="submit__btn" type="submit" :disabled="disabled">
    <slot/>
    <slot name="icon"></slot>
  </button>
</template>

<style scoped>
.submit__btn {
  background: var(--accent-main);
  color: var(--text-light);
  padding: 12px;
  width: 100%;
  border: none;
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
.submit__btn:hover {
  background: var(--accent-hover);
  transform: scale(1.01);
}
.submit__btn:disabled{
  background-color: var(--accent-disabled);
  transform: none;
}
</style>