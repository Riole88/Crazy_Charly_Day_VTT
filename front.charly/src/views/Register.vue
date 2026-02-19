<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const API = import.meta.env.VITE_API
const router = useRouter()

const form = ref({
  firstName: '',
  lastName: '',
  email: '',
  password: '',
  confirmPassword: '',
})

const loading = ref(false)
const error = ref('')
const submitted = ref(false)

async function handleSubmit() {
  error.value = ''

  if (form.value.password !== form.value.confirmPassword) {
    error.value = 'Les mots de passe ne correspondent pas.'
    return
  }

  loading.value = true

  try {
    const res = await fetch(`${API}/signup`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: form.value.email,
        password: form.value.password,
        firstName: form.value.firstName,
        lastName: form.value.lastName,
      }),
    })

    const data = await res.json()

    if (!res.ok) {
      throw new Error(data.error ?? 'Erreur lors de l\'inscription')
    }

    submitted.value = true
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container">
    <h2>Créer un compte</h2>

    <div v-if="submitted" class="success">
      Compte créé avec succès !
      <div class="success-actions">
        <button @click="router.push('/login')">Se connecter</button>
      </div>
    </div>

    <form v-else @submit.prevent="handleSubmit">
      <div class="row">
        <div class="field">
          <label>Prénom</label>
          <input v-model="form.firstName" type="text" placeholder="Marie" required />
        </div>
        <div class="field">
          <label>Nom</label>
          <input v-model="form.lastName" type="text" placeholder="Dupont" required />
        </div>
      </div>

      <div class="field">
        <label>Email</label>
        <input v-model="form.email" type="email" placeholder="marie@exemple.com" required />
      </div>

      <div class="field">
        <label>Mot de passe</label>
        <input v-model="form.password" type="password" placeholder="••••••••" required />
      </div>

      <div class="field">
        <label>Confirmer le mot de passe</label>
        <input v-model="form.confirmPassword" type="password" placeholder="••••••••" required />
      </div>

      <p v-if="error" class="error">{{ error }}</p>

      <button type="submit" class="btn-submit" :disabled="loading">
        {{ loading ? 'Création...' : 'Créer mon compte' }}
      </button>
    </form>

    <p class="toggle">
      Déjà un compte ?
      <a href="#" @click.prevent="router.push('/login')">Se connecter</a>
    </p>
  </div>
</template>

<style scoped>
.container {
  max-width: 460px;
  margin: 60px auto;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

h2 {
  margin-bottom: 24px;
}

.row {
  display: flex;
  gap: 16px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 16px;
  flex: 1;
}

label {
  font-weight: bold;
  font-size: 14px;
}

input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.btn-submit {
  width: 100%;
  padding: 10px;
  margin-top: 8px;
  background: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
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
  margin-top: 14px;
}

.success-actions button {
  padding: 8px 16px;
  border: 1px solid #4caf50;
  border-radius: 4px;
  background: white;
  cursor: pointer;
  color: #2e7d32;
}

.toggle {
  margin-top: 20px;
  text-align: center;
  font-size: 14px;
}

.toggle a {
  color: #333;
  font-weight: bold;
}

.error {
  color: #c62828;
  font-size: 14px;
  margin-bottom: 12px;
}

@media (max-width: 600px) {
  .row { flex-direction: column; }
}
</style>
