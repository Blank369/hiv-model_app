<template>
  <div v-if="loading" class="loading-container">
    <progress
        class="progress-bar"
        :value="progress"
        :max="max"
    />

    <p v-if="showText" class="loading-text">
      {{ text }} {{ progress }}%
    </p>
  </div>
</template>

<script setup>
import { ref, watch, onUnmounted } from 'vue'

const props = defineProps({
  loading: Boolean,

  completed: Boolean,

  text: {
    type: String,
    default: 'Выполняется расчёт...'
  },

  max: {
    type: Number,
    default: 100
  },

  showText: {
    type: Boolean,
    default: true
  }
})

const progress = ref(0)

let interval = null


function startProgress() {
  progress.value = 10

  interval = setInterval(() => {
    if (progress.value < 90) {
      progress.value += 5
    }
  }, 200)
}

function stopProgress() {
  clearInterval(interval)

  progress.value = 100

  setTimeout(() => {
    progress.value = 0
  }, 400)
}

watch(
    () => props.loading,
    (loading) => {
      if (loading) {
        startProgress()
      } else {
        stopProgress()
      }
    }
)

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<style scoped>
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.progress-bar {
  width: 100%;
  height: 10px;
  border-radius: var(--radius-md);
  overflow: hidden;
}

.progress-bar::-webkit-progress-bar {
  background-color: var(--border-color);
  border-radius: var(--radius-md);
}

.progress-bar::-webkit-progress-value {
  background-color: var(--accent-main);
  border-radius: var(--radius-md);
  transition: width 0.2s ease;
}

.progress-bar.indeterminate::-webkit-progress-value {
  background-color: var(--accent-main);
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0% { opacity: 0.4; }
  50% { opacity: 1; }
  100% { opacity: 0.4; }
}

.loading-text {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin: 0;
}
</style>