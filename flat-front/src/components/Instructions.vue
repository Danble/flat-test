<template>
  <div>
    <h5>Instructions</h5>
    <div class="card horizontal">
      <div class="card-stacked">
        <div class="card-content">
          <p>Select a branch to check detail info.</p>
          <p>Checkboxes are for merging branches</p>
          <label class="to-merge"></label>
          <hr>
          <p class="for-label">to merge</p>
          <label class="merge-into"></label>
          <p class="for-label" style="margin-top:1.1rem">merge into</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
label {
  position: absolute;
  left: 30px;
  margin-top: 1rem;
  border: 1px solid rgb(110, 110, 110);
  width: 1.5rem;
  height: 1.5rem;
}

.card-stacked {
  height: 12rem;
}

.for-label {
  margin-top: 1rem;
}

.merge-into {
  background-color: #4e5f7a;
}

.to-merge {
  background-color: #26a69a;
}
</style>