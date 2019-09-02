/* DaTouWang URL: www.datouwang.com */
Vue.component("carousel", {
  template: "#v-carousel",
  data() {
    return {
      currentOffset: 0,
      windowSize: 5,
      paginationFactor: 220,// 页码滚动距离
      items: [
        {name: 'Tycoon Thai', tag: "Thai"},
        {name: 'Ippudo', tag: "Japanese"},
        {name: 'Milano', tag: "Pizza"},
        {name: 'Tsing Tao', tag: "Chinese"},
        {name: 'Frances', tag: "French"},
        {name: 'Burma Superstar', tag: "Burmese"},
        {name: 'Salt and Straw', tag: "Ice cream"},
        {name: 'Salt and Straw', tag: "Ice cream"},
        {name: 'Salt and Straw', tag: "Ice cream"},
      ]
    }
  },
  computed: {
    atEndOfList() {

      return this.currentOffset <= (this.paginationFactor * -1) * (this.items.length - this.windowSize);
    },
    atHeadOfList() {
      return this.currentOffset === 0;
    },
  },
  methods: {
    moveCarousel(direction) {
      // Find a more elegant way to express the :style. consider using props to make it truly generic
      if (direction === 1 && !this.atEndOfList) {
        this.currentOffset -= this.paginationFactor;
      } else if (direction === -1 && !this.atHeadOfList) {
        this.currentOffset += this.paginationFactor;
      }
    },
  }
});

new Vue({
  el:"#app"
});