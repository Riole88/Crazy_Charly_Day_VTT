<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  email: '',
  password: '',
})

function handleSubmit() {
  console.log('Login:', form.value)
  // TODO: appel API /api/login
}
</script>

<template>
  <div class="container">
    <h2>Connexion</h2>

    <form @submit.prevent="handleSubmit">
      <div class="field">
        <label>Email</label>
        <input v-model="form.email" type="email" placeholder="exemple@mail.com" required />
      </div>

      <div class="field">
        <label>Mot de passe</label>
        <input v-model="form.password" type="password" placeholder="••••••••" required />
      </div>

      <button type="submit">Se connecter</button>
    </form>

    <p class="toggle">
      Pas encore de compte ?
      <a href="#" @click.prevent="router.push('/register')">S'inscrire</a>
    </p>
  </div>
</template>

<style scoped>
.container {
  max-width: 400px;
  margin: 60px auto;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

h2 {
  margin-bottom: 24px;
}

.field {
  display: flex;
  flex-direction: column;
  margin-bottom: 16px;
  gap: 6px;
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

button {
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

button:hover {
  background: #555;
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
</style>
