import mongoose, { Document, Model, Schema } from 'mongoose';

export interface INote extends Document {
  content: string;
  userId: string;
  createdAt: Date;
}

const NoteSchema: Schema = new Schema({
  content: {
    type: String,
    required: true,
  },
  userId: {
    type: String,
    required: true,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

export const Note: Model<INote> = mongoose.models.Note || mongoose.model<INote>('Note', NoteSchema);
