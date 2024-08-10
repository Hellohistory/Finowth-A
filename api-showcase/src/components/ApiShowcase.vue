<template>
  <div class="container">
    <aside class="sidebar">
      <h2>{{ apiTitle }}</h2>
      <input type="text" v-model="searchQuery" placeholder="搜索API..." class="search-box" />
      <h2>API 在线测试列表</h2>
      <ul>
        <li v-for="api in filteredApiInfo" :key="api.api_path" @click="selectApi(api)" :class="{ selected: api.api_path === selectedApi?.api_path }" class="api-item">
          <span class="api-path">{{ api.api_path }}</span>
        </li>
      </ul>
    </aside>
    <main class="main-content">
      <div v-if="selectedApi" class="api-details">
        <h2 v-html="highlight(selectedApi.api_name)"></h2>
        <p class="description" v-html="highlight(selectedApi.description)"></p>
        <div class="select-container">
          <label for="language">选择语言:</label>
          <select v-model="selectedLanguage" @change="updateCodeSample(selectedApi)" class="select-box">
            <option v-for="lang in languages" :key="lang" :value="lang">{{ lang }}</option>
          </select>
        </div>
        <div class="code-container">
          <pre><code v-html="highlightedCodeSample" class="hljs"></code></pre>
          <button @click="copyCode" class="copy-button">{{ copyButtonText }}</button>
        </div>

        <div v-if="selectedApi.method.toUpperCase() === 'POST'" class="params-section">
          <h3>输入参数</h3>
          <form @submit.prevent="runApi(selectedApi)">
            <div v-for="(param, index) in selectedApi.parameters" :key="index" class="form-group">
              <label :for="param.name" v-html="highlight(param.title || param.name)"></label>
              <small v-html="highlight(param.description)"></small>
              <input v-model="postParams[param.name]" @input="updateCodeSample(selectedApi)" :id="param.name" :type="param.type === 'integer' ? 'number' : 'text'" class="form-control"/>
            </div>
            <button type="submit" class="run-button">运行</button>
          </form>
        </div>

        <button v-else @click="runApi(selectedApi)" class="run-button">运行</button>

        <div v-if="loading" class="loading">正在请求...</div>

        <div v-if="responseData[selectedApi.api_path]" class="response-section">
          <h3>响应:</h3>
          <pre><code v-html="highlightedResponse" class="hljs"></code></pre>
        </div>

        <div v-if="error" class="error-section">
          <h3>错误:</h3>
          <pre>{{ error }}</pre>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import {generateCodeSample} from './CodeSamples';
import hljs from 'highlight.js';
import 'highlight.js/styles/default.css';

export default {
  data() {
    return {
      apiTitle: 'FinData API',
      apiInfo: [],
      searchQuery: '',
      selectedApi: null,
      selectedLanguage: 'Python',
      languages: ['Python', 'Rust', 'Java', 'JavaScript', 'C++', 'Go', 'PHP', 'R', 'Ruby', 'C#', 'Lua', 'VB', 'Kotlin', 'MATLAB', 'Swift', 'Objective-C', 'Dart', 'Perl', 'Scala', 'Haskell', 'Elixir', 'Shell', 'TypeScript', 'Groovy', 'F#'],
      codeSample: '',
      responseData: {},
      postParams: {},
      error: null,
      loading: false,
      copyButtonText: '复制'
    };
  },
  computed: {
    filteredApiInfo() {
      return this.apiInfo.filter(api =>
          this.searchFields(api).some(field =>
              field.toLowerCase().includes(this.searchQuery.toLowerCase())
          )
      );
    },
    highlightedCodeSample() {
      return hljs.highlight(this.codeSample, {language: this.selectedLanguage.toLowerCase()}).value;
    },
    highlightedResponse() {
      const response = this.responseData[this.selectedApi?.api_path];
      if (response) {
        return hljs.highlight(JSON.stringify(response, null, 2), {language: 'json'}).value;
      }
      return '';
    }
  },
  async created() {
    const response = await axios.get('http://localhost:36925/api_info');
    this.apiInfo = response.data;
  },
  methods: {
    searchFields(api) {
      return [api.api_path, api.description, api.api_name || ''];
    },
    selectApi(api) {
      this.selectedApi = api;
      this.postParams = {};
      this.updateCodeSample(api);
      this.error = null;
    },
    updateCodeSample(api) {
      const params = {};
      api.parameters.forEach(param => {
        params[param.name] = this.postParams[param.name] || '';
      });
      this.codeSample = generateCodeSample(api, this.selectedLanguage, params);
    },
    async runApi(api) {
      this.loading = true;
      try {
        const params = {};
        api.parameters.forEach(param => {
          params[param.name] = this.postParams[param.name] || '';
        });

        const response = await axios({
          method: api.method.toLowerCase(),
          url: `http://localhost:36925${api.api_path}`,
          data: api.method.toUpperCase() === 'POST' ? params : {}
        });
        this.responseData = {...this.responseData, [api.api_path]: response.data};
        this.error = null;
      } catch (err) {
        this.error = err.response ? err.response.data : err.message;
      } finally {
        this.loading = false;
      }
    },
    copyCode() {
      const textarea = document.createElement('textarea');
      textarea.value = this.codeSample;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      this.copyButtonText = '已复制';
      setTimeout(() => {
        this.copyButtonText = '复制';
      }, 2000);
    },
    highlight(text) {
      if (!this.searchQuery) return text;
      const regex = new RegExp(`(${this.escapeRegex(this.searchQuery)})`, 'gi');
      return text.replace(regex, (match) => `<span class="highlight">${match}</span>`);
    },
    escapeRegex(string) {
      return string.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
    }
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.copy-button {
  margin-top: 10px;
}

.highlight {
  background-color: yellow;
}

.copy-button {
  margin-top: 10px;
}

.container {
  display: flex;
  font-family: 'Roboto', sans-serif;
  height: 100vh;
  background-color: #f0f2f5;
}

.sidebar {
  width: 300px;
  padding: 20px;
  border-right: 1px solid #ccc;
  overflow-y: auto;
  background-color: #fff;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.main-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  cursor: pointer;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  transition: background-color 0.3s;
}

li:hover {
  background-color: #e0e0e0;
}

li.selected {
  background-color: #007bff;
  border-color: #0056b3;
  color: white;
}

.api-item .api-path {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.api-details {
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search-box {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.select-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.select-box {
  margin-left: 10px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.code-container {
  position: relative;
  margin-bottom: 20px;
}

pre {
  background-color: #f8f9fa;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  white-space: pre-wrap;
  word-wrap: break-word;
  position: relative;
}

pre code {
  display: block;
}

.copy-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.description {
  white-space: pre-wrap;
  word-wrap: break-word;
  margin-bottom: 20px;
}

.params-section {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  font-weight: 700;
  margin-bottom: 5px;
}

.form-group small {
  display: block;
  margin-bottom: 10px;
  color: #6c757d;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.run-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.run-button:hover {
  background-color: #0056b3;
}

.loading {
  margin-top: 10px;
  color: #007bff;
}

.response-section {
  margin-top: 20px;
}

.error-section {
  margin-top: 20px;
  color: #dc3545;
}

h2 {
  font-weight: 700;
  margin-bottom: 20px;
}

label {
  font-weight: 700;
}
</style>
