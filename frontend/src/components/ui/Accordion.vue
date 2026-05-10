<template>
  <details :open="isOpen">
    <summary>
      <slot name="icon"></slot>
      <slot name="title">
        {{ title }}
      </slot>
    </summary>
    <div class="content">
      <slot/>
    </div>
  </details>
</template>

<script setup>

defineProps({
  title: String,
  isOpen: {
    type: Boolean,
    default: false
  }
})
</script>

<style scoped>
details {
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  margin-bottom: 12px;
  background: var(--bg-card);
}
summary {
  padding: 12px 16px;
  font-weight: 600;
  cursor: pointer;
  list-style: none;
  display: flex;
  align-items: center;
  gap: 8px;
  user-select: none;
  border-radius: var(--radius-md);
}
summary::before {
  content: '▶';
  font-size: 12px;
  color: #2c3e50;
  transition: transform 0.2s ease;
  margin-right: 8px;
}
details[open] summary::before {
  transform: rotate(90deg);
}
summary::-webkit-details-marker {
  display: none;
}
.content {
  padding: 12px 16px 16px 16px;
  border-top: 1px solid #eee;
}
</style>