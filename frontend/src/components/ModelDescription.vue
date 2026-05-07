<template>
  <div class="model-card">
    <div class="card-header">
      <IconQuestion class="header-icon"/>
      <h2>Математическая модель взаимодействия ВИЧ и иммунной системы человека</h2>
    </div>
    <div class="card-body">
      <Accordion title="Уравнения модели" :isOpen="true">
        <template #icon>
          <IconBook/>
        </template>

        <Accordion>
          <template #title>
            <code class="equation">
              dT/dt = λ + r·T·(1 - (T+I+L)/T<sub>max</sub>) - d<sub>T</sub>·T - (1-ε<sub>inf</sub>)·β·V·T
            </code>
          </template>
          <div class="description">динамика здоровых CD4⁺-лимфоцитов</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">λ</span>
              <span class="param-desc">скорость поступления наивных CD4⁺-клеток из тимуса</span>
            </div>
            <div class="param-item">
              <span class="param-name">r</span>
              <span class="param-desc">максимальная скорость пролиферации CD4⁺-клеток</span>
            </div>
            <div class="param-item">
              <span class="param-name">T_max</span>
              <span class="param-desc">максимальная ёмкость популяции CD4⁺</span>
            </div>
            <div class="param-item">
              <span class="param-name">d_T</span>
              <span class="param-desc">скорость естественной гибели CD4⁺</span>
            </div>
            <div class="param-item">
              <span class="param-name">β</span>
              <span class="param-desc">константа скорости инфицирования клеток вирусом</span>
            </div>
            <div class="param-item">
              <span class="param-name">ε_inf</span>
              <span class="param-desc">эффективность ингибиторов заражения (АРТ)</span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dL/dt = ρ·(1-ε<sub>inf</sub>)·β·V·T - a·L - δ<sub>L</sub>·L
            </code>
          </template>
          <div class="description">динамика латентно инфицированных клеток</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">ρ</span>
              <span class="param-desc">доля заражённых клеток, идущих в латентный резервуар</span>
            </div>
            <div class="param-item">
              <span class="param-name">a</span>
              <span class="param-desc">скорость реактивации латентных клеток</span>
            </div>
            <div class="param-item">
              <span class="param-name">δ_L</span>
              <span class="param-desc">скорость гибели латентно инфицированных клеток</span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dI/dt = (1-ρ)·(1-ε<sub>inf</sub>)·β·V·T + a·L - δ<sub>I</sub>·I - κ·C·I
            </code>
          </template>
          <div class="description">динамика продуктивно инфицированных клеток</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">δ_I</span>
              <span class="param-desc">скорость гибели продуктивно инфицированных клеток</span>
            </div>
            <div class="param-item">
              <span class="param-name">κ</span>
              <span class="param-desc">скорость уничтожения инфицированных клеток CTL</span>
            </div>
            <div class="param-item">
              <span class="param-name">C</span>
              <span class="param-desc">концентрация эффекторных CTL-клеток</span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dV/dt = (1-ε<sub>prod</sub>)·p·I - c·V - φ·C·V
            </code>
          </template>
          <div class="description">динамика свободных вирусных частиц</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">p</span>
              <span class="param-desc">скорость продукции вируса инфицированными клетками</span>
            </div>
            <div class="param-item">
              <span class="param-name">c</span>
              <span class="param-desc">скорость естественного клиренса вируса</span>
            </div>
            <div class="param-item">
              <span class="param-name">φ</span>
              <span class="param-desc">скорость нейтрализации вируса CTL</span>
            </div>
            <div class="param-item">
              <span class="param-name">ε_prod</span>
              <span class="param-desc">эффективность ингибиторов продукции вируса (АРТ)</span>
            </div>
          </div>
        </Accordion>

        <Accordion>
          <template #title>
            <code class="equation">
              dC/dt = s<sub>C</sub> + (α·T·C)/(T·C + h) - d<sub>C</sub>·C - η<sub>C</sub>·C·I/(I+q)
            </code>
          </template>
          <div class="description">динамика эффекторных иммунных клеток (CTL)</div>
          <div class="params-grid">
            <div class="param-item">
              <span class="param-name">s_C</span>
              <span class="param-desc">постоянный приток CTL-клеток</span>
            </div>
            <div class="param-item">
              <span class="param-name">α</span>
              <span class="param-desc">скорость активации CTL при стимуляции CD4⁺</span>
            </div>
            <div class="param-item">
              <span class="param-name">h</span>
              <span class="param-desc">константа насыщения активации</span>
            </div>
            <div class="param-item">
              <span class="param-name">d_C</span>
              <span class="param-desc">скорость естественной гибели CTL</span>
            </div>
            <div class="param-item">
              <span class="param-name">η_C</span>
              <span class="param-desc">скорость истощения CTL при высокой нагрузке</span>
            </div>
            <div class="param-item">
              <span class="param-name">q</span>
              <span class="param-desc">порог истощения иммунитета</span>
            </div>
          </div>
        </Accordion>
      </Accordion>
      <Accordion title="Параметры антиретровирусной терапии">
        <template #icon>
          <IconMicroscope/>
        </template>
        <div class="params-grid">
          <div class="param-item">
            <span class="param-name">ε_inf</span>
            <span class="param-desc">Эффективность препаратов, блокирующих заражение клеток</span>
          </div>
          <div class="param-item">
            <span class="param-name">ε_prod</span>
            <span class="param-desc">Эффективность препаратов, снижающих продукцию вируса</span>
          </div>
        </div>
        <div class="therapy-modes">
          <h4 class="therapy-modes__title">Рассматриваемые сценарии:</h4>
          <div class="mode">
            <span class="mode-badge">WITHOUT</span>
            <span>Без терапии</span>
          </div>
          <div class="mode">
            <span class="mode-badge">THERAPY</span>
            <span>Включение на n-ый день</span>
          </div>
          <div class="mode">
            <span class="mode-badge">INTERRUPTION</span>
            <span>Приём с периодичностью γ</span>
          </div>
          <div class="mode">
            <span class="mode-badge">RESISTANCE</span>
            <span>Развитие резистентности</span>
          </div>
        </div>
      </Accordion>
    </div>
  </div>
</template>
<script setup lang="ts">
import IconBook from "@/components/icons/IconBook.vue";
import Accordion from "@/components/ui/Accordion.vue";
import IconMicroscope from "@/components/icons/IconMicroscope.vue";
import IconQuestion from "@/components/icons/IconQuestion.vue";
</script>

<style>
.model-card {
  background: var(--bg-card);
  border-radius: var(--radius-lg, 12px);
  border: 1px solid var(--border-color);
  overflow: hidden;
  margin-bottom: 20px;
}

.card-body{
  padding: 1rem;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  background: var(--bg-hover);
  border-bottom: 1px solid var(--border-color);
}

.card-header h2 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}

.header-icon {
  width: 24px;
  height: 24px;
  color: var(--color-primary);
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

</style>