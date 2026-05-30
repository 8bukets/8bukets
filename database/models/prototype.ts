import mongoose, { Schema, Document } from 'mongoose';
import { Prototype } from '../../antigravity/schemas/prototype';

// Omit the 'id' field from the Mongoose document interface since Mongoose uses '_id'
export interface IPrototype extends Omit<Prototype, 'id'>, Omit<Document, '_id'> {
    _id: string;
}

const PrototypeSchema = new Schema<IPrototype>({
    _id: { type: String, default: () => crypto.randomUUID() },
    name: { type: String, required: true, minlength: 3 },
    description: { type: String, required: false },
    version: {
        type: String,
        required: true,
        match: /^\d+\.\d+\.\d+$/
    },
    status: {
        type: String,
        required: true,
        enum: ['draft', 'active', 'archived'],
        default: 'draft'
    },
    features: { type: [String], default: [] },
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
}, {
    timestamps: true, // Automatically manages createdAt and updatedAt
});

// We only want to create the model once to avoid OverwriteModelError during hot reloads
export const PrototypeModel = mongoose.models.Prototype || mongoose.model<IPrototype>('Prototype', PrototypeSchema);
