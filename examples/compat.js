const crypto = require('crypto');
const checksum = crypto.createHash('md5').update('example').digest('hex');
