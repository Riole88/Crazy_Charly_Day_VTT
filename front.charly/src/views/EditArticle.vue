<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { categories, tranches, etats } from '@/constants/articles'

const API = import.meta.env.VITE_API
const route = useRoute()
const router = useRouter()

const form = ref({
  designation: '',
  category: '',
  age: '',
  state: '',
  price: '',
  weight: '',
})

const original = ref({})
const loading = ref(true)
const saving = ref(false)
const error = ref('')
const success = ref(false)

onMounted(async () => {
  try {
    const res = await fetch(`${API}/articles/${route.params.id}`)
    if (!res.ok) throw new Error('Article introuvable')
    const article = await res.json()
    original.value = { ...article }
    form.value = {
      designation: article.designation,
      category: article.category,
      age: article.age,
      state: article.state,
      price: article.price,
      weight: article.weight,
    }
  } catch (e) {
    error.value = "Impossible de charger l'article."
    console.error(e)
  } finally {
    loading.value = false
  }
})

async function handleSubmit() {
  error.value = ''
  saving.value = true

  // N'envoie que les champs modifiés
  const payload = {}
  if (form.value.designation !== original.value.designation) payload.designation = form.value.designation
  if (form.value.category !== original.value.category) payload.category = form.value.category
  if (form.value.age !== original.value.age) payload.age = form.value.age
  if (form.value.state !== original.value.state) payload.state = form.value.state
  if (Number(form.value.price) !== original.value.price) payload.price = parseFloat(form.value.price)
  if (Number(form.value.weight) !== original.value.weight) payload.weight = parseInt(form.value.weight)

  if (Object.keys(payload).length === 0) {
    error.value = 'Aucune modification détectée.'
    saving.value = false
    return
  }

  try {
    const res = await fetch(`${API}/articles/${route.params.id}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
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
    saving.value = false
  }
}
</script>

<template>
  <div class="container">
    <button class="btn-retour" @click="router.push(`/articles/${route.params.id}`)">
      ← Retour à l'article
    </button>

    <h2>Modifier l'article</h2>

    <p v-if="loading" class="info">Chargement...</p>

    <div v-else-if="success" class="success">
      Article modifié avec succès !
      <div class="success-actions">
        <button @click="router.push(`/articles/${route.params.id}`)">Voir l'article</button>
        <button @click="router.push('/articles')">Retour au catalogue</button>
      </div>
    </div>

    <form v-else @submit.prevent="handleSubmit">
      <div class="field">
        <label>Désignation</label>
        <input v-model="form.designation" type="text" required />
      </div>

      <div class="row">
        <div class="field">
          <label>Catégorie</label>
          <select v-model="form.category" required>
            <option v-for="c in categories" :key="c.code" :value="c.code">
              {{ c.code }} — {{ c.label }}
            </option>
          </select>
        </div>

        <div class="field">
          <label>Tranche d'âge</label>
          <select v-model="form.age" required>
            <option v-for="t in tranches" :key="t.code" :value="t.code">
              {{ t.label }}
            </option>
          </select>
        </div>

        <div class="field">
          <label>État</label>
          <select v-model="form.state" required>
            <option v-for="e in etats" :key="e.code" :value="e.code">
              {{ e.label }}
            </option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="field">
          <label>Prix (€)</label>
          <input v-model="form.price" type="number" min="0" step="1" required />
        </div>

        <div class="field">
          <label>Poids (g)</label>
          <input v-model="form.weight" type="number" min="0" step="1" required />
        </div>
      </div>

      <p v-if="error" class="error">{{ error }}</p>

      <button type="submit" class="btn-submit" :disabled="saving">
        {{ saving ? 'Enregistrement...' : 'Enregistrer les modifications' }}
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

.info { color: #666; }
.error { color: #c62828; font-size: 14px; margin-bottom: 12px; }

@media (max-width: 600px) {
  .row { flex-direction: column; }
}
</style>
