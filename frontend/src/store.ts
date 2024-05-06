import { configureStore } from '@reduxjs/toolkit';
import { conversationSlice } from './conversation/conversationSlice';
import {
  prefListenerMiddleware,
  prefSlice,
} from './preferences/preferenceSlice';

const key = localStorage.getItem('dociqApiKey');
const prompt = localStorage.getItem('dociqPrompt');
const doc = localStorage.getItem('dociqRecentDocs');
const chunks = localStorage.getItem('dociqChunks');

const store = configureStore({
  preloadedState: {
    preference: {
      apiKey: key ?? '',
      chunks: JSON.parse(chunks ?? '2').toString(),
      selectedDocs: doc !== null ? JSON.parse(doc) : null,
      prompt:
        prompt !== null
          ? JSON.parse(prompt)
          : { name: 'default', id: 'default', type: 'private' },
      conversations: null,
      sourceDocs: [
        {
          location: '',
          language: '',
          name: 'default',
          version: '',
          date: '',
          description: '',
          docLink: '',
          fullName: '',
          model: '1.0',
        },
      ],
      modalState: 'INACTIVE',
    },
  },
  reducer: {
    preference: prefSlice.reducer,
    conversation: conversationSlice.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(prefListenerMiddleware.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export default store;

// TODO : use https://redux-toolkit.js.org/tutorials/typescript#define-typed-hooks everywere instead of direct useDispatch

// TODO : streamline async state management
