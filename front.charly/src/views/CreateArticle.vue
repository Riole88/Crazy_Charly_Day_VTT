<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { categories, tranches, etats } from '@/constants/articles'

const API = import.meta.env.VITE_API
const router = useRouter()

const form = ref({
  designation: '',
  category: '',
  age: '',
  state: '',
  price: '',
  weight: '',
})

const loading = ref(false)
const error = ref('')
const success = ref(false)

async function handleSubmit() {
  error.value = ''
  loading.value = true

  try {
    const res = await fetch(`${API}/articles`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        designation: form.value.designation,
        category: form.value.category,
        age: form.value.age,
        state: form.value.state,
        price: parseFloat(form.value.price),
        weight: parseInt(form.value.weight),
      }),
    })

    if (!res.ok) {
      const err = await res.json()
      throw new Error(err.message ?? 'Erreur serveur')
    }

    success.value = true
  } catch (e) {
    error.value = e.message ?? "Une erreur est survenue."
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container">
    <button class="btn-retour" @click="router.push('/articles')">← Retour au catalogue</button>

    <h2>Ajouter un article</h2>

    <div v-if="success" class="success">
      Article ajouté avec succès !
      <div class="success-actions">
        <button @click="() => { success = false; form = { designation: '', category: '', age: '', state: '', price: '', weight: '' } }">Ajouter un autre article</button>
        <button @click="router.push('/articles')">Voir le catalogue</button>
      </div>
    </div>

    <form v-else @submit.prevent="handleSubmit">
      <div class="field">
        <label>Désignation *</label>
        <input v-model="form.designation" type="text" placeholder="Ex: Monopoly Junior" required />
      </div>

      <div class="row">
        <div class="field">
          <label>Catégorie *</label>
          <select v-model="form.category" required>
            <option value="" disabled>Choisir...</option>
            <option v-for="c in categories" :key="c.code" :value="c.code">
              {{ c.code }} — {{ c.label }}
            </option>
          </select>
        </div>

        <div class="field">
          <label>Tranche d'âge *</label>
          <select v-model="form.age" required>
            <option value="" disabled>Choisir...</option>
            <option v-for="t in tranches" :key="t.code" :value="t.code">
              {{ t.label }}
            </option>
          </select>
        </div>

        <div class="field">
          <label>État *</label>
          <select v-model="form.state" required>
            <option value="" disabled>Choisir...</option>
            <option v-for="e in etats" :key="e.code" :value="e.code">
              {{ e.label }}
            </option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="field">
          <label>Prix (€) *</label>
          <input v-model="form.price" type="number" min="0" step="1" placeholder="Ex: 8" required />
        </div>

        <div class="field">
          <label>Poids (g) *</label>
          <input v-model="form.weight" type="number" min="0" step="1" placeholder="Ex: 400" required />
        </div>
      </div>

      <p v-if="error" class="error">{{ error }}</p>

      <button type="submit" class="btn-submit" :disabled="loading">
        {{ loading ? 'Enregistrement...' : 'Ajouter l\'article' }}
      </button>
    </form>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 40px auto;
  padding: 0 20px;
}

h2 {
  margin-bottom: 24px;
}

.btn-retour {
  background: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px 14px;
  cursor: pointer;
  font-size: 14px;
  margin-bottom: 24px;
  color: #333;
}

.btn-retour:hover {
  background: #f5f5f5;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 16px;
  flex: 1;
}

label {
  font-size: 14px;
  font-weight: 600;
  color: #444;
}

input,
select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.row {
  display: flex;
  gap: 16px;
}

.btn-submit {
  width: 100%;
  padding: 12px;
  background: #333;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 15px;
  cursor: pointer;
  margin-top: 8px;
}

.btn-submit:hover:not(:disabled) {
  background: #555;
}

.btn-submit:disabled {
  opacity: 0.6;
  cursor: default;
}

.success {
  padding: 16px;
  border: 1px solid #4caf50;
  border-radius: 6px;
  color: #2e7d32;
  background: #f1f8f1;
}

.success-actions {
  display: flex;
  gap: 12px;
  margin-top: 14px;
}

.success-actions button {
  padding: 8px 16px;
  border: 1px solid #4caf50;
  border-radius: 4px;
  background: white;
  cursor: pointer;
  color: #2e7d32;
  font-size: 14px;
}

.error {
  color: #c62828;
  font-size: 14px;
  margin-bottom: 12px;
}

@media (max-width: 600px) {
  .row {
    flex-direction: column;
  }
}
</style>
