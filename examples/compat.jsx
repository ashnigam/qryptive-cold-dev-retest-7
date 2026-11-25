import { createHash } from 'node:crypto';
export const fingerprint = createHash('sha1').update('parcel').digest('hex');
