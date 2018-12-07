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
                <!-- <ParticipantInfo></ParticipantInfo> -->
                <v-layout row wrap v-for="(participant, key) in participants">
                    <v-flex xs6>
                        <v-text-field prepend-icon="person" name="name" label="Name" type="text" v-model="participants[key].name"></v-text-field>
                    </v-flex>
                    <v-spacer></v-spacer> 
                    <v-flex xs6>
                        <v-text-field prepend-icon="email" name="email" label="Email" type="email" v-model="participants[key].email"></v-text-field>
                    </v-flex>             
                </v-layout>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="addParticipant(key)">Add</v-btn>
              <v-btn color="red" @click="rudolf()">Send</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import ParticipantInfo from "./ParticipantInfo";
export default {
  name: "HelloWorld",
  components: {
    ParticipantInfo
  },
  data(){
    return {
      participants: []
    }
  },
  methods: {
    addParticipant() {
      this.participants.push({ name: '', email: ''});
    },
    rudolf() {
      let data = []
      this.participants.forEach(user => {
        console.log(user.name, user.email)
        data.push([user.name, user.email])
      }); 
      axios.post("https://8goak50z6d.execute-api.eu-west-1.amazonaws.com/Lab-ServerlessSecretSanta/santa", {
        data: data
      })
      .then(response => {})
      .catch(e => {
        this.errors.push(e)
      });
    }
  },
  created(){
    this.addParticipant();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
