<template>
  <div>
    <md-table v-model="users" :table-header-color="tableHeaderColor">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="編號">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="發布單位">{{ item.name }}</md-table-cell>
        <md-table-cell md-label="公告標題">{{ item.title }}</md-table-cell>
        <md-table-cell md-label="發布日期">{{ item.date }}</md-table-cell>
        <!-- <md-table-cell md-label="發布日期">{{ item.city }}</md-table-cell> -->
      </md-table-row>
    </md-table>
  </div>
</template>

<script>

export default {
  name: "ordered-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      selected: [],
      users: [],
    };
  },
  mounted() {
    axios.get('http://localhost:3000/OrderedTable_data').then((res)=>{
      //console.log(res.data);
      this.users=res.data;
    })
  },
};
</script>
