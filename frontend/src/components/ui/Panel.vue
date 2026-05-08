<template>
  <div class="container">
    <div class="container__header">
      <slot name="icon"></slot>
      <h2>
        {{ title }}
      </h2>
    </div>
    <div class="container__body">
      <slot/>
    </div>
  </div>
</template>

<script setup>

defineProps({
  title: String
})

</script>

<style>
.container {
  background: var(--bg-card);
  border-radius: var(--radius-lg, 12px);
  border: 1px solid var(--border-color);
  overflow: hidden;
  margin-bottom: 20px;
}

.container__body {
  padding: 1rem;
}

.container__header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  background: var(--bg-hover);
  border-bottom: 1px solid var(--border-color);
}

.container__header h2 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}
</style>
