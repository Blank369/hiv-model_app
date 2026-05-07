<template>
  <div>
    <Accordion title="О математической модели взаимодействия ВИЧ и иммунной системы человека" :isOpen="true">
      <template #icon>
        <IconBook/>
      </template>
      <p>Здесь будет описание уравнений и переменных...</p>
    </Accordion>
  </div>
</template>
<script setup lang="ts">
import IconBook from "@/components/icons/IconBook.vue";
import Accordion from "@/components/ui/Accordion.vue";
</script>