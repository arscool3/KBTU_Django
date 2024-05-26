// useStore.ts
import { create } from 'zustand';
import axiosInstance from '../services/api';
import {
    User,
    Link,
    Click,
    Category,
    Tag,
    LinkUsage,
    LinkInput,
} from '../core/interfaces';

interface StoreState {
    user: User | null;
    links: Link[];
    clicks: Click[];
    categories: Category[];
    tags: Tag[];
    linkUsages: LinkUsage[];
    setUser: (user: User) => void;
    setLinks: (links: Link[]) => void;
    setClicks: (clicks: Click[]) => void;
    setCategories: (categories: Category[]) => void;
    setTags: (tags: Tag[]) => void;
    setLinkUsages: (linkUsages: LinkUsage[]) => void;
    fetchLinks: () => Promise<void>;
    fetchCategories: () => Promise<void>;
    fetchTags: () => Promise<void>;
    fetchClicks: () => Promise<void>;
    addLink: (link: LinkInput) => Promise<void>;
    deleteLink: (id: number) => Promise<void>;
    updateLink: (id: number, link: LinkInput) => Promise<void>;
    postClick: (linkId: number) => Promise<void>;
    register: (userData: any) => Promise<void>;
    login: (credentials: { username: string; password: string }) => Promise<boolean>;
    logout: () => void;
    refreshToken: () => Promise<void>;
}

const useLinkStore = create<StoreState>((set) => ({
    user: null,
    links: [],
    clicks: [],
    categories: [],
    tags: [],
    linkUsages: [],
    setUser: (user: User) => set({ user }),
    setLinks: (links: Link[]) => set({ links }),
    setClicks: (clicks: Click[]) => set({ clicks }),
    setCategories: (categories: Category[]) => set({ categories }),
    setTags: (tags: Tag[]) => set({ tags }),
    setLinkUsages: (linkUsages: LinkUsage[]) => set({ linkUsages }),

    fetchLinks: async () => {
        try {
            const response = await axiosInstance.get('/links/');
            set({ links: response.data });
        } catch (error) {
            console.error('Error fetching links:', error);
        }
    },
    fetchCategories: async () => {
        try {
            const response = await axiosInstance.get('/categories/');
            set({ categories: response.data });
        } catch (error) {
            console.error('Error fetching categories:', error);
        }
    },
    fetchTags: async () => {
        try {
            const response = await axiosInstance.get('/tags/');
            set({ tags: response.data });
        } catch (error) {
            console.error('Error fetching tags:', error);
        }
    },
    fetchClicks: async () => {
        try {
            const response = await axiosInstance.get('/clicks/');
            set({ clicks: response.data });
        } catch (error) {
            console.error('Error fetching clicks:', error);
        }
    },
    addLink: async (link: LinkInput) => {
        try {
            const response = await axiosInstance.post('/links/', link);
            set((state) => ({ links: [...state.links, response.data] }));
        } catch (error) {
            console.error('Error adding link:', error);
        }
    },
    deleteLink: async (id: number) => {
        try {
            await axiosInstance.delete(`/links/${id}/`);
            set((state) => ({
                links: state.links.filter((link) => link.id !== id),
            }));
        } catch (error) {
            console.error('Error deleting link:', error);
        }
    },
    updateLink: async (id: number, link: LinkInput) => {
        try {
            const response = await axiosInstance.put(`/links/${id}/`, link);
            set((state) => ({
                links: state.links.map((l) => (l.id === id ? response.data : l)),
            }));
        } catch (error) {
            console.error('Error updating link:', error);
        }
    },
    postClick: async (linkId: number) => {
        try {
            const response = await axiosInstance.post('/clicks/', {
                link: linkId,
                timestamp: new Date().toISOString(),
            });
            set((state) => ({ clicks: [...state.clicks, response.data] }));
        } catch (error) {
            console.error('Error posting click:', error);
        }
    },
    register: async (userData: any) => {
        try {
            const response = await axiosInstance.post('/register/', userData);
            set({ user: response.data });
        } catch (error) {
            console.error('Error registering:', error);
        }
    },
    login: async (credentials: { username: string; password: string }) => {
        try {
            const response = await axiosInstance.post('/login/', credentials);
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            set({ user: response.data.user });
            return true;
        } catch (error) {
            console.error('Error logging in:', error);
            return false;
        }
    },
    logout: () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        set({ user: null });
    },
    refreshToken: async () => {
        try {
            const refreshToken = localStorage.getItem('refresh_token');
            if (!refreshToken) {
                throw new Error('No refresh token available');
            }
            const response = await axiosInstance.post('/token/refresh/', {
                refresh: refreshToken,
            });
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            set({ user: response.data.user });
        } catch (error) {
            console.error('Error refreshing token:', error);
            set({ user: null });
        }
    },
}));

export default useLinkStore;
