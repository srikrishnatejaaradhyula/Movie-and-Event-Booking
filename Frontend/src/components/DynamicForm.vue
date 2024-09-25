<template>
    <div class=" container">
        <div class="row">
            <div class="col-md-12">
                <h1>Dynamic Form</h1>
            </div>
            <div class="col-md-12">
                <button class="primary-button" @click="IsModalForm = true">Create Dynamic Form</button>
            </div>
            <div class="col-md-12">
                {{ form }}
            </div>
            <div class="row col-md-12" v-for="f in form">
                <div class="col-md-12" v-if="f.type == 'checkbox'">
                    <div class="col-md-12">
                        <h3>{{ f.checkboxLabel }}</h3>
                    </div>
                    <div class="row col-md-12">
                        <div class="col-md-4" v-for="c in f.checkboxCount">
                                <input class="form-check-input" type="checkbox" :value="f.checkboxName[c-1]" v-model="f.value" name="checkbox" id="check">
                                <label class="form-check-label" for="check">{{ f.checkboxLabel[c-1] }}</label>
                        </div>
                    </div>
                </div>
                <div class="col-md-12" v-else-if="f.type == 'radio'">
                    <div class="row col-md-12">
                        <div class="col-md-4" v-for="r in f.radioCount">
                            <input class="form-check-input" type="radio" :value="f.radioName[r-1]" v-model="f.value" name="radio" id="radio">
                            <label class="form-check-label" for="radio">{{ f.radioLabel[r-1] }}</label>
                        </div>
                    </div>
                </div>
                <div class="col-md-12" v-else-if="f.type == 'select'">
                    <div class="form-floating col-md-12">
                        <select class="form-select" aria-label="Default select example" v-model="f.value">
                            <option v-for="o in f.optionCount" :value="f.optionName[o-1]">{{ f.optionLabel[o-1] }}</option>
                        </select>
                    </div>
                </div>
                <div class="row col-md-12 m-1" v-else-if="f.type == 'textarea'">
                    <div class="form-floating col-md-12">
                        <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px" v-model="f.value"></textarea>
                        <label for="floatingTextarea2">{{ f.inputLabel }}</label>
                    </div>
                </div>
                <div class="col-md-12" v-else>
                    <div class="form-floating col-md-12">
                        <input :type=f.type class="form-control" id="floatingInput" placeholder=" " v-model="f.value" :placeholder="f.inputLabel">
                        <label for="floatingInput">{{ f.inputLabel }}</label>
                    </div>
                </div>
            </div>

            <Teleport to="#modal2">
                <div class="modal-bg  " v-if="IsModalForm">
                    <div class="mt-4 overflow-y-auto position-relative container h-50 w-50  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                        <div class=" position-absolute top-0 end-0 "> 
                            <button @click="IsModalForm = false" class="m-2 border-0 rounded-5 ">
                                <i class="bi bi-x-lg" style="color:brown"></i>
                            </button>
                        </div>
                        <div class=" container">
                            <div class="row">
                                <div class="form-floating col-md-12">
                                    <select class="form-select" id="forType" aria-label="Default select example" v-model="type" >
                                        <option value="text">Text</option>
                                        <option value="email">E-mail</option>
                                        <option value="number">Number</option>
                                        <option value="date">Date</option>
                                        <option value="time">Time</option>
                                        <option value="password">Password</option>
                                        <option value="textarea">Textarea</option>
                                        <option value="select">Select</option>
                                        <option value="checkbox">Checkbox</option>
                                        <option value="radio">Radio</option>
                                    </select>
                                    <label for="forType" >Select Type of Input Field </label>
                                </div>
                                <div class="col-md-12 m-1" v-if="type =='checkbox'" onchange="type">
                                    <div class="form-floating col-md-12 m-1" >
                                        <input type="number" class="form-control" id="floatingInput" v-model="checkboxCount" placeholder="Number of checkbox">
                                        <label for="floatingInput">Number of checkbox</label>
                                    </div>
                                    <!-- {{ checkboxLabel }} -->
                                    <div class="row col-md-12 m-1" v-for="c in checkboxCount">
                                        <div class="form-floating col-md-6">
                                            <input type="text" class="form-control" id="floatingInput" v-model="checkboxLabel[c-1]" placeholder="Checkbox label">
                                            <label for="floatingInput">Checkbox label</label>
                                        </div>
                                        <div class="form-floating col-md-6">
                                            <input type="text" class="form-control" id="floatingInput" v-model="checkboxName[c-1]" placeholder="Checkbox name">
                                            <label for="floatingInput">Checkbox name</label>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-12 m-1"  v-else-if="type =='radio'" onchange="type">
                                    <div class="form-floating  col-md-12 m-1" >
                                        <input type="number" class="form-control" id="floatingInput" v-model="radioCount" placeholder="Number of radio">
                                        <label for="floatingInput">Number of radio</label>
                                    </div>
                                    <div class="row col-md-12 m-1" v-for="r in radioCount">
                                        <div class="form-floating  col-md-6">
                                            <input type="text" class="form-control" id="floatingInput" v-model="radioLabel[r-1]" placeholder="Radio label">
                                            <label for="floatingInput">Radio label</label>
                                        </div>
                                        <div class="form-floating col-md-6">
                                            <input type="text" class="form-control" id="floatingInput" v-model="radioName[r-1]" placeholder="Radio name">
                                            <label for="floatingInput">Radio name</label>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-12 m-1"  v-else-if="type =='select'" onchange="type">
                                    <div class="form-floating col-md-12 m-1" >
                                        <input type="number" class="form-control" id="floatingInput" v-model="optionCount" placeholder="Number of select">
                                        <label for="floatingInput">Number of select</label>
                                    </div>
                                    <div class="row col-md-12 m-1" v-for="s in optionCount">
                                        <div class="form-floating  col-md-6">
                                            <input type="text" class="form-control" id="floatingInput" v-model="optionLabel[s-1]" placeholder="Select label">
                                            <label for="floatingInput">Select label</label>
                                        </div>
                                        <div class="form-floating col-md-6">
                                            <input type="text" class="form-control" id="floatingInput" v-model="optionName[s-1]" placeholder="Select name">
                                            <label for="floatingInput">Select name</label>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="row col-md-12 m-1" v-else>
                                    <div class="form-floating col-md-6">
                                        <input type="text" class="form-control" id="floatingInput" v-model="inputLabel" placeholder="Select label">
                                        <label for="floatingInput">Select label</label>
                                    </div>
                                    <div class="form-floating col-md-6">
                                        <input type="text" class="form-control"  id="floatingInput" v-model="inputName" placeholder="Select name">
                                        <label for="floatingInput">Select name</label>
                                    </div>
                                    </div>

                            </div>
                        </div>
                        
                        <div class="container mt-4">
                            <div class="row " >
                                <div class="col-6 text-center " >
                                    <button type="button" @click="AddToForm"  class="btn btn-success " >
                                        Add form
                                    </button>
                                </div>
                                <div class="col-6 text-center ">
                                    <button type="button" @click="IsModalForm = false"  class="btn btn-danger">Cancel</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </Teleport>
        </div>
    </div>
</template>

<script setup>

const type = ref()
const IsModalForm = ref(false)
const checkboxCount = ref()
const radioCount = ref()
const optionCount = ref()
const checkboxLabel = ref([])
const checkboxName = ref([])
const radioLabel = ref([])
const radioName = ref([])
const optionLabel = ref([])
const optionName = ref([])
const inputLabel = ref()
const inputName = ref()

const form = ref([])

const AddToForm = () =>{
    if (type.value == 'checkbox') {
        form.value.push({
            type: type.value,
            checkboxCount: checkboxCount.value,
            checkboxLabel: checkboxLabel.value,
            checkboxName: checkboxName.value,
            value: []
        })
        console.log(form.value)
        type.value = ''
        checkboxCount.value = ''
        checkboxLabel.value = []
        checkboxName.value = []
        IsModalForm.value = false
    }
    if (type.value == 'radio') {
        console.log(radioCount.value)
        console.log(radioLabel.value)
        console.log(radioName.value)
        form.value.push({
            type: type.value,
            radioCount: radioCount.value,
            radioLabel: radioLabel.value,
            radioName: radioName.value,
            value: ''
        })
        console.log(form.value)
        type.value = ''
        radioCount.value = ''
        radioLabel.value = []
        radioName.value = []
        IsModalForm.value = false
    }
    if (type.value == 'select') {
        form.value.push({
            type: type.value,
            optionCount: optionCount.value,
            optionLabel: optionLabel.value,
            optionName: optionName.value,
            value: ''
        })
        console.log(form.value)
        type.value = ''
        optionCount.value = ''
        optionLabel.value = []
        optionName.value = []
        IsModalForm.value = false
    }
    if (type.value == 'text' || type.value == 'email' || type.value == 'number' || type.value == 'date' || type.value == 'password' || type.value == 'textarea'){
        form.value.push({
            type: type.value,
            inputLabel: inputLabel.value,
            inputName: inputName.value,
            value: ''
        })
        console.log(form.value)
        type.value = ''
        inputLabel.value = ''
        inputName.value = ''
        IsModalForm.value = false
    }

}

</script>

<style  scoped>
.form-floating input[type="text"],
.form-floating input[type="number"],
.form-floating input[type="password"],
.form-floating input[type="time"],
.form-floating input[type="date"],
.form-floating input[type="email"],
.form-floating select,
.form-floating textarea {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0.21);
}


</style>