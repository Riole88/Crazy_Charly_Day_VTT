import { ref, computed } from 'vue'

const token = ref(localStorage.getItem('token') ?? null)
const tokenType = ref(localStorage.getItem('tokenType') ?? 'Bearer')

export function useAuth() {
  const isAuthenticated = computed(() => !!token.value)

  function setToken(newToken, type = 'Bearer') {
    token.value = newToken
    tokenType.value = type
    localStorage.setItem('token', newToken)
    localStorage.setItem('tokenType', type)
  }

  function clearToken() {
    token.value = null
    tokenType.value = 'Bearer'
    localStorage.removeItem('token')
    localStorage.removeItem('tokenType')
  }

  function authHeader() {
    return token.value ? { Authorization: `${tokenType.value} ${token.value}` } : {}
  }

  return { token, tokenType, isAuthenticated, setToken, clearToken, authHeader }
}
