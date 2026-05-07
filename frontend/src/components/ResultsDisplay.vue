<template>
  <div>
    <Accordion title="Результаты моделирования" :isOpen="true">
      <template #icon>
        <IconGraph/>
      </template>
      <p>После запуска здесь появятся графики и статистика...</p>
    </Accordion>
  </div>
</template>
<script setup lang="ts">
import Accordion from "@/components/ui/Accordion.vue";
import IconGraph from "@/components/icons/IconGraph.vue";
</script>