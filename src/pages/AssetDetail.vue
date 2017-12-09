<template>
    <div class="goods">
        <van-swipe class="goods-swipe">
            <van-swipe-item v-for="thumb in goods.thumb" :key="thumb">
                <img :src="thumb">
            </van-swipe-item>
        </van-swipe>
        <van-cell-group>
            <van-cell>
                <div class="goods-title">{{ goods.title }}</div>
                <!-- <div class="goods-price">{{ formatPrice(goods.price) }}</div> -->
            </van-cell>
            <van-cell class="goods-express">
                <van-col span="14">债券机构：北京xxxxx有限责任公司</van-col>
                <van-col span="14">债务人（企业）：明广振</van-col>
                <van-col span="14">保证人（企业）：小贾</van-col>
                <van-col span="14">抵押人：小贾</van-col>
            </van-cell>
        </van-cell-group>
        <van-cell-group>
            <van-cell>
                <div class="goods-title">资产亮点</div>
                <van-cell class="goods-express">
                    <van-col span="24">诉讼情况：已经诉讼完毕，请放心购买</van-col>
                    <van-col span="24">资产保全情况：保全的特别好跟新的一样</van-col>
                    <van-col span="24">核心卖点：棒棒棒！！！</van-col>
                    <van-col span="24">周边配套：医院、学校、公交、地铁、飞机、航空母舰</van-col>
                    <van-col span="24">小区介绍：世外桃源，布莱克西</van-col>
                </van-cell>
            </van-cell>
            <van-cell>
                <div class="goods-title">受公理事项</div>
                <van-cell class="goods-express">
                    <van-col span="12">联系人：明广振</van-col>
                    <van-col span="12">联系电话：13311036150</van-col>
                    <van-col span="24">传真：010-8830-3114</van-col>
                    <van-col span="24">通讯地址：北京市朝阳区望京soho-T3-1701</van-col>
                </van-cell>
            </van-cell>
            <van-cell>
                <div class="goods-title">交易对象及声明</div>
                <van-cell class="goods-express">
                    <van-col span="24">交易对象：须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。须为大陆信用极好的用户。</van-col>
                    <van-col span="24">声明：以上信息纯属虚构，仅供参考。以上信息纯属虚构，仅供参考。以上信息纯属虚构，仅供参考。以上信息纯属虚构，仅供参考。以上信息纯属虚构，仅供参考。以上信息纯属虚构，仅供参考。</van-col>
                </van-cell>
            </van-cell>
        </van-cell-group>
        <van-goods-action>
            <van-goods-action-mini-btn icon="like-o">
                收藏
            </van-goods-action-mini-btn>
            <van-goods-action-mini-btn icon="chat">
                客服
            </van-goods-action-mini-btn>
            <van-goods-action-big-btn primary>
                报价
            </van-goods-action-big-btn>
        </van-goods-action>
    </div>
</template>
<script>
import {
    Tag,
    Col,
    Icon,
    Cell,
    CellGroup,
    Swipe,
    SwipeItem,
    GoodsAction,
    GoodsActionBigBtn,
    GoodsActionMiniBtn
} from 'vant';

export default {
    components: {
        [Tag.name]: Tag,
        [Col.name]: Col,
        [Icon.name]: Icon,
        [Cell.name]: Cell,
        [CellGroup.name]: CellGroup,
        [Swipe.name]: Swipe,
        [SwipeItem.name]: SwipeItem,
        [GoodsAction.name]: GoodsAction,
        [GoodsActionBigBtn.name]: GoodsActionBigBtn,
        [GoodsActionMiniBtn.name]: GoodsActionMiniBtn
    },

    data() {
        return {
            goods: {
                title: '华润公园九里，小户型低总价',
                price: 2680,
                express: '免运费',
                remain: 19,
                thumb: [
                    'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=4093669240,825203326&fm=27&gp=0.jpg',
                    'http://a3.att.hudong.com/65/07/01300000248343122451075325224.jpg'
                ]
            }
        };
    },

    methods: {
        formatPrice() {
            return '¥' + (this.goods.price / 100).toFixed(2);
        }
    }
};
</script>
<style lang="less">
.goods {
    padding-bottom: 50px;

    &-swipe {
        img {
            width: .7.5rem;
            height: 7.5rem;
            display: block;
        }
    }

    &-title {
        font-size: 16px;
    }

    &-price {
        color: #f44;
    }

    &-express {
        color: #999;
        font-size: 12px;
        padding: 5px 15px 5px 0;
    }

    &-cell-group {
        margin: 15px 0;

        .van-cell__value {
            color: #999;
        }
    }
}
</style>