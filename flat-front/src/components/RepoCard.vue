import RepoCard from '@components/RepoCard';
<template>
  <div class="row">
    <div class="col">
      <div class="card blue-grey darken-1">
        <div class="card-content white-text">
          <span class="card-title">Message: {{commit.message}}</span>
          <p>Commit: {{commit.commit}}</p>
          <br>
          <p>Date: {{commit.date}}</p>
        </div>
        <div class="card-action">
          <p>Author: {{commit.author}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.col {
  display: flex;
  justify-content: center;
  width:100%
}

.card {
  width: 60%;
}

.card-action > p {
  color: rgb(226, 226, 99);
}
</style>

<script>
export default {
  props: ["commit"]
}
</script>