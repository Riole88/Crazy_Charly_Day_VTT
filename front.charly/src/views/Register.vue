<script setup>
import { ref } from 'vue'

const categories = ref([
  { code: 'SOC', label: 'Jeux de société' },
  { code: 'FIG', label: 'Figurines et poupées' },
  { code: 'CON', label: 'Jeux de construction' },
  { code: 'EXT', label: "Jeux d'extérieur" },
  { code: 'EVL', label: "Jeux d'éveil et éducatifs" },
  { code: 'LIV', label: 'Livres jeunesse' },
])

const tranches = [
  { code: 'BB', label: 'BB — 0-3 ans (bébé)' },
  { code: 'PE', label: 'PE — 3-6 ans (petit enfant)' },
  { code: 'EN', label: 'EN — 6-10 ans (enfant)' },
  { code: 'AD', label: 'AD — 10+ ans (adolescent)' },
]

const form = ref({
  nom: '',
  prenom: '',
  email: '',
  tranche: '',
})

function moveUp(index) {
  if (index === 0) return
  const arr = categories.value
  ;[arr[index - 1], arr[index]] = [arr[index], arr[index - 1]]
}

function moveDown(index) {
  if (index === categories.value.length - 1) return
  const arr = categories.value
  ;[arr[index + 1], arr[index]] = [arr[index], arr[index + 1]]
}

const submitted = ref(false)
const error = ref('')

async function handleSubmit() {
  error.value = ''
  if (!form.value.tranche) {
    error.value = "Veuillez sélectionner la tranche d'âge de votre enfant."
    return
  }

  const payload = {
    nom: form.value.nom,
    prenom: form.value.prenom,
    email: form.value.email,
    tranche: form.value.tranche,
    preferences: categories.value.map((c) => c.code),
  }

  try {
    const res = await fetch('/api/abonnes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
    if (!res.ok) throw new Error('Erreur serveur')
    submitted.value = true
  } catch (e) {
    error.value = "Une erreur est survenue. Veuillez réessayer."
    console.error(e)
  }
}
</script>

<template>
  <div class="container">
    <h2>Inscription abonné</h2>

    <div v-if="submitted" class="success">
      Inscription enregistrée ! Votre box sera composée prochainement.
    </div>

    <form v-else @submit.prevent="handleSubmit">
      <!-- Identité -->
      <fieldset>
        <legend>Vos informations</legend>

        <div class="field">
          <label>Nom</label>
          <input v-model="form.nom" type="text" placeholder="Dupont" required />
        </div>

        <div class="field">
          <label>Prénom</label>
          <input v-model="form.prenom" type="text" placeholder="Marie" required />
        </div>

        <div class="field">
          <label>Email</label>
          <input v-model="form.email" type="email" placeholder="marie@exemple.com" required />
        </div>
      </fieldset>

      <!-- Tranche d'âge -->
      <fieldset>
        <legend>Tranche d'âge de votre enfant</legend>
        <div class="radio-group">
          <label v-for="t in tranches" :key="t.code">
            <input v-model="form.tranche" type="radio" :value="t.code" />
            {{ t.label }}
          </label>
        </div>
      </fieldset>

      <!-- Préférences -->
      <fieldset>
        <legend>Ordre de préférence des catégories</legend>
        <p class="hint">Classez les catégories de la plus souhaitée à la moins souhaitée.</p>

        <ul class="pref-list">
          <li v-for="(cat, index) in categories" :key="cat.code">
            <span class="rank">{{ index + 1 }}</span>
            <span class="cat-label">{{ cat.label }} <small>({{ cat.code }})</small></span>
            <div class="actions">
              <button type="button" @click="moveUp(index)" :disabled="index === 0">▲</button>
              <button type="button" @click="moveDown(index)" :disabled="index === categories.length - 1">▼</button>
            </div>
          </li>
        </ul>
      </fieldset>

      <p v-if="error" class="error">{{ error }}</p>

      <button type="submit" class="submit-btn">S'inscrire</button>
    </form>
  </div>
</template>

<style scoped>
.container {
  max-width: 520px;
  margin: 40px auto;
  padding: 30px;
}

h2 {
  margin-bottom: 24px;
}

fieldset {
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 16px;
  margin-bottom: 20px;
}

legend {
  font-weight: bold;
  padding: 0 8px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 14px;
}

label {
  font-size: 14px;
}

input[type='text'],
input[type='email'] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.radio-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.radio-group label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.hint {
  font-size: 13px;
  color: #666;
  margin-bottom: 12px;
}

.pref-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.pref-list li {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #fafafa;
}

.rank {
  font-weight: bold;
  min-width: 20px;
  color: #333;
}

.cat-label {
  flex: 1;
  font-size: 14px;
}

.cat-label small {
  color: #888;
}

.actions {
  display: flex;
  gap: 6px;
}

.actions button {
  padding: 4px 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background: white;
  cursor: pointer;
  font-size: 12px;
}

.actions button:disabled {
  opacity: 0.3;
  cursor: default;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background: #333;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 15px;
  cursor: pointer;
}

.submit-btn:hover {
  background: #555;
}

.success {
  padding: 16px;
  border: 1px solid #4caf50;
  border-radius: 6px;
  color: #2e7d32;
  background: #f1f8f1;
}

.error {
  color: #c62828;
  font-size: 14px;
  margin-bottom: 12px;
}

@media (max-width: 600px) {
  .container {
    padding: 16px;
    margin: 10px;
  }
}
</style>
