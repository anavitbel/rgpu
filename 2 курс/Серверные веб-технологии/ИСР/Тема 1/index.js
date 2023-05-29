const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
const urlencodedParser = bodyParser.urlencoded({extended: false});

const Schema = mongoose.Schema;

const productScheme = new Schema({
    name: String,
    type: String,
    amount: {
        number: Number,
        unit: String
    }
});

mongoose.connect("mongodb connection string", { useUnifiedTopology: true, useNewUrlParser: true });

const Product = mongoose.model('products', productScheme);

app.get('/products', (req, res) => {
    void Product.find({}, (err, data) => res.send(data));
})
.post('/products/new', urlencodedParser, (req, res) => {
    const product = new Product(req.body);
    product.save(err => {
        res.send({'status': err ? err : 'success'});
    });
})
.post('/products/update/:id', urlencodedParser, (req, res) => {
    let id = mongoose.Types.ObjectId(req.params.id);
    Product.updateOne({'_id': id}, req.body, (err, result) => {
        res.send({'status': err ? err : 'success'});
    });
})
.post('/products/delete/:id', urlencodedParser, (req, res) => {
    let id = mongoose.Types.ObjectId(req.params.id);
    Product.deleteOne({'_id': id}, (err, result) => {
        res.send({'status': err ? err : 'success'});
    });
});

app.listen();