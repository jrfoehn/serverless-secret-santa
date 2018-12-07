<template>
    <div>
        <v-layout row wrap>
            <v-flex xs6>
                <v-text-field prepend-icon="person" name="name" label="Name" type="text"></v-text-field>
            </v-flex>
            <v-spacer></v-spacer> 
            <v-flex xs6>
                <v-text-field prepend-icon="email" name="email" label="Email" type="email"></v-text-field>
            </v-flex>             
        </v-layout>
    </div>
</template>

<script>
export default {
    name: "ParticipantInfo",
    props: {
    }
};
</script>
