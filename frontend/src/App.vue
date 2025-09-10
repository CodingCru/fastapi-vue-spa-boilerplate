<template>
  <div id="app">
    <header>
      <h1>FastAPI + Vue 3 SPA Boilerplate</h1>
    </header>
    
    <main>
      <div class="container">
        <section class="hero">
          <h2>Welcome to your new application!</h2>
          <p>This is a minimal boilerplate for rapid development with FastAPI and Vue 3.</p>
        </section>

        <section class="status">
          <h3>Service Status</h3>
          <div v-if="loading">Loading...</div>
          <div v-else-if="error" class="error">{{ error }}</div>
          <div v-else class="status-grid">
            <div class="status-card">
              <h4>Frontend</h4>
              <span class="status-indicator success">✓</span>
              <p>Vue 3 SPA Running</p>
            </div>
            <div class="status-card">
              <h4>Backend API</h4>
              <span class="status-indicator" :class="apiStatus ? 'success' : 'error'">
                {{ apiStatus ? '✓' : '✗' }}
              </span>
              <p>{{ apiStatus ? 'FastAPI Connected' : 'FastAPI Disconnected' }}</p>
            </div>
          </div>
        </section>

        <section class="endpoints">
          <h3>Available Endpoints</h3>
          <ul>
            <li><code>GET /</code> - Root endpoint</li>
            <li><code>GET /health</code> - Health check</li>
            <li><code>GET /api/health</code> - API health check</li>
            <li><code>GET /api/status</code> - Service status</li>
          </ul>
        </section>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      loading: true,
      error: null,
      apiStatus: false
    }
  },
  async mounted() {
    await this.checkApiStatus()
  },
  methods: {
    async checkApiStatus() {
      try {
        const response = await fetch('/api/health')
        const data = await response.json()
        this.apiStatus = data.status === 'healthy'
      } catch (error) {
        console.error('Failed to check API status:', error)
        this.apiStatus = false
        this.error = 'Failed to connect to backend API'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f5f5;
}

#app {
  min-height: 100vh;
}

header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem 0;
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  font-weight: 300;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.hero {
  text-align: center;
  margin-bottom: 3rem;
}

.hero h2 {
  color: #333;
  margin-bottom: 1rem;
  font-size: 2rem;
}

.hero p {
  color: #666;
  font-size: 1.1rem;
}

.status, .endpoints {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.status h3, .endpoints h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.status-card {
  background: #f8f9fa;
  border-radius: 6px;
  padding: 1.5rem;
  text-align: center;
  border: 1px solid #e9ecef;
}

.status-card h4 {
  margin-bottom: 1rem;
  color: #495057;
}

.status-indicator {
  display: inline-block;
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.status-indicator.success {
  color: #28a745;
}

.status-indicator.error {
  color: #dc3545;
}

.endpoints ul {
  list-style: none;
}

.endpoints li {
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  background: #f8f9fa;
  border-radius: 4px;
  border-left: 3px solid #667eea;
}

.endpoints code {
  font-family: 'Monaco', 'Menlo', monospace;
  font-weight: bold;
  color: #667eea;
}

.error {
  color: #dc3545;
  text-align: center;
  padding: 1rem;
  background: #f8d7da;
  border-radius: 4px;
  border: 1px solid #f5c6cb;
}
</style>