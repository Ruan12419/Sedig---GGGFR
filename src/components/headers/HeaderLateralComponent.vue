<template>
    <section class="header column" style="align-items: center; justify-content: center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b3/Eletrobras.png">
    </section>
</template>

<script>
export default {
    name: "HeaderLateralComponent",
}

</script>

<style scoped>
.header {
    height: 100vh !important;
    width: 350px;
    background-color: #6BC9DB;
}

.column {
    display: flex;
    flex-direction: column;
}

img {
    width: 80%;
    margin-bottom: 180px;
}
</style>