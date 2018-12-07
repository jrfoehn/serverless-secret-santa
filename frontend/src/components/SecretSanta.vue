<template>
  <div>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="red">
              <v-toolbar-title>Secret Santa Participants</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field prepend-icon="person" name="name" label="Name" type="text"></v-text-field>
                <v-text-field prepend-icon="alternate_email" name="email" label="Email" type="email"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary">Add Participant</v-btn>
              <v-btn color="red">Send</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
