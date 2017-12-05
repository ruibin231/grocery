<template>
  <div class="card-list">
    <van-card
      v-for="(item, index) in propertyList"
      :title="item.title"
      :desc="item.desc"  
      num="2"
      price="2.00"
      :thumb="imageURL"
    >
      <div slot="footer">
        <van-button size="mini">收藏</van-button>
        <van-button size="mini">报价</van-button>
      </div>
    </van-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        imageURL: 'http://img.yzcdn.cn/upload_files/2017/07/02/af5b9f44deaeb68000d7e4a711160c53.jpg',
        propertyList: [
          {title: '资产1', desc: '描述1'},
          {title: '资产2', desc: '描述2'},
          {title: '资产3', desc: '描述3'},
        ]
      }
    }
  }
</script>

<style>
  .card-list {
    margin-top: 1em;
  }
</style>
