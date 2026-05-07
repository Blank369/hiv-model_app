<template>
  <details :open="isOpen">
    <summary>
      <slot name="icon"></slot>
      {{ title }}
    </summary>
    <div class="content">
      <slot/>
    </div>
  </details>
</template>

<script setup>
import IconCommunity from "@/components/icons/IconCommunity.vue";

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
  border: 1px solid #e0e0e0;
  border-radius: 10px;
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
  border-radius: 10px;
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