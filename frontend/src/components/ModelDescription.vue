<template>
  <Panel title="Mathematical Model HIV–immune system interaction">
    <template #icon>
      <IconQuestion/>
    </template>
    <div class="card-body">
      <Accordion title="Model Equations" :isOpen="isOpen">
        <template #icon>
          <IconBook/>
        </template>

        <Accordion>
          <template #title>
            <code class="equation">
              dT/dt = λ + r·T·(1 - (T+I+L)/T<sub>max</sub>) - d<sub>T</sub>·T - (1-ε<sub>inf</sub>(t))·β·V·T
            </code>
          </template>
          <div class="description">dynamics of uninfected CD4+ T cells</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">λ</span>
              <span class="param-desc">natural influx of CD4+ cells from the thymus</span>
            </div>
            <div class="param-item">
              <span class="param-name">r</span>
              <span class="param-desc">rate of homeostatic proliferation of CD4+ T cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">T_max</span>
              <span class="param-desc">effective carrying capacity of the CD4+ T-cell population</span>
            </div>
            <div class="param-item">
              <span class="param-name">d_T</span>
              <span class="param-desc">natural death rate of CD4+ cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">β</span>
              <span class="param-desc">infection rate coefficient for CD4+ T cells by free virions</span>
            </div>
            <div class="param-item">
              <span class="param-name">ε_inf</span>
              <span class="param-desc"><a class="anchor" href="#einf">efficacy of infection inhibitors (ART)</a></span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dL/dt = ρ·(1-ε<sub>inf</sub>(t))·β·V·T - a·L - δ<sub>L</sub>·L
            </code>
          </template>
          <div class="description">dynamics of latently infected CD4+ T cells</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">ρ</span>
              <span class="param-desc">fraction of newly infected cells entering the latent state</span>
            </div>
            <div class="param-item">
              <span class="param-name">a</span>
              <span class="param-desc">reactivation rate of latently infected cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">δ_L</span>
              <span class="param-desc">natural death rate of latently infected cells </span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dI/dt = (1-ρ)·(1-ε<sub>inf</sub>(t))·β·V·T + a·L - δ<sub>I</sub>·I - κ·C·I
            </code>
          </template>
          <div class="description">dynamics of productively infected CD4+ T cells</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">δ_I</span>
              <span class="param-desc">natural death rate of productively infected cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">κ</span>
              <span class="param-desc">coefficient of cytotoxic killing of productively infected cells</span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dV/dt = (1-ε<sub>prod</sub>(t))·p·I - c·V - φ·C·V
            </code>
          </template>
          <div class="description">dynamics of free HIV virions</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">p</span>
              <span class="param-desc">rate of virion production by a productively infected cell</span>
            </div>
            <div class="param-item">
              <span class="param-name">c</span>
              <span class="param-desc">natural clearance rate of free virions</span>
            </div>
            <div class="param-item">
              <span class="param-name">φ</span>
              <span class="param-desc">coefficient of immune-mediated neutralisation of free virus</span>
            </div>
            <div class="param-item">
              <span class="param-name">ε_prod</span>
              <span class="param-desc"><a class="anchor" href="#eprod">efficacy of viral production inhibitors (ART)</a></span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dC/dt = s<sub>C</sub> + (α·T·C)/(T·C + h) - d<sub>C</sub>·C - η<sub>C</sub>·C·I/(I+q)
            </code>
          </template>
          <div class="description">dynamics of immune effector cells (CTLs)</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">s_C</span>
              <span class="param-desc">basal influx of immune effector cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">α</span>
              <span class="param-desc">maximum rate of effector immune-response stimulation</span>
            </div>
            <div class="param-item">
              <span class="param-name">h</span>
              <span class="param-desc">saturation parameter for immune stimulation</span>
            </div>
            <div class="param-item">
              <span class="param-name">d_C</span>
              <span class="param-desc">natural death rate of immune effector cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">η_C</span>
              <span class="param-desc">maximum rate of functional exhaustion of immune effector cells</span>
            </div>
            <div class="param-item">
              <span class="param-name">q</span>
              <span class="param-desc">characteristic infected-cell level for saturation of the exhaustion effect</span>
            </div>
          </div>
        </Accordion>
      </Accordion>
      <Accordion title="Antiretroviral Therapy">
        <template #icon>
          <IconMicroscope/>
        </template>
        <div class="params-grid">
          <div class="param-item">
            <span class="param-name">ε_inf</span>
            <span class="param-desc" id="einf">The efficacy of therapy in reducing the formation of newly infected cells</span>
          </div>
          <div class="param-item">
            <span class="param-name">ε_prod</span>
            <span class="param-desc" id="eprod">The efficacy of therapy in suppressing the production of new viral particles</span>
          </div>
        </div>
        <div class="therapy-modes">
          <h4 class="therapy-modes__title">Treatment scenarios:</h4>
          <div class="mode">
            <span class="mode-badge">WITHOUT</span>
            <span>No therapy</span>
          </div>
          <div class="mode">
            <span class="mode-badge">THERAPY</span>
            <span>Treatment initiation on day γ</span>
          </div>
          <div class="mode">
            <span class="mode-badge">INTERRUPTION</span>
            <span>Periodically varying treatment efficacy</span>
          </div>
          <div class="mode">
            <span class="mode-badge">RESISTANCE</span>
            <span>Decline in treatment efficacy</span>
          </div>
        </div>
      </Accordion>
    </div>
  </Panel>
</template>
<script setup lang="ts">
import IconBook from "@/components/icons/IconBook.vue";
import Accordion from "@/components/ui/Accordion.vue";
import IconMicroscope from "@/components/icons/IconMicroscope.vue";
import IconQuestion from "@/components/icons/IconQuestion.vue";
import Panel from "@/components/ui/Panel.vue";
import {computed} from "vue";

const props = defineProps({
  isResultsReady: Boolean
})

const isOpen = computed(() => {
  return !props.isResultsReady
})
</script>

<style>
.card-header h2 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}

.description {
  color: var(--color-primary);
  margin-bottom: 1rem;
  font-weight: 500;
  padding: 0.5rem;
  background: var(--bg-surface);
  border-radius: var(--radius-sm);
}

.params-grid {
  padding: 0.5rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.param-item {
  display: flex;
  align-items: baseline;
  gap: 8px;
  padding: 4px 0;
  border-bottom: 1px dashed var(--border-color);
}

.param-name {
  font-weight: 700;
  font-family: monospace;
  color: var(--color-primary);
  min-width: 50px;
}

.param-desc {
  font-size: 0.85rem;
  color: var(--text-primary);
  flex: 1;
}

.therapy-modes {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.therapy-modes__title{
  margin-top: 1rem;
}

.mode {
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 8px 12px;
  background: var(--bg-sidebar);
  border-radius: var(--radius-sm);
}

.mode-badge {
  font-family: monospace;
  font-weight: 700;
  font-size: 0.75rem;
  background: var(--accent-main);
  color: white;
  padding: 2px 8px;
  border-radius: 16px;
  min-width: 100px;
  text-align: center;
}

.mode span:last-child {
  font-size: 0.85rem;
  color: var(--text-primary);
}

.equation {
  font-family: 'Courier New', 'SF Mono', 'Fira Code', monospace;
  border-radius: var(--radius-sm);
  display: inline-block;
  letter-spacing: 0.5px;
}

.equation sub {
  font-size: 0.7rem;
}

.anchor {
  text-decoration: none;
  color: var(--color-primary);
}

</style>