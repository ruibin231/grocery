<template>
  <div>
    <van-nav-bar title="标题" leftText="返回" leftArrow>
      <van-icon name="search" slot="right" />
    </van-nav-bar>
    <div class="content">
      <!-- 主要内容 -->
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {}
    },
    components: {
      
    }
  }
</script>
