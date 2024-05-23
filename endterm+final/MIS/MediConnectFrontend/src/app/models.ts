export interface Profile {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  password: string;
  is_doctor: boolean;
  specialty?: number;
  specialty_name: string;
  clinic_location?: string;
  iin_bin?: string;              
  license_number?: string;       
  license_issued_date?: string;  
  license_status?: string;
}
  
export interface Doctor {
  id: number;
  specialty: number | null;
  specialty_name: string;
  clinic_location: string | null;
  profile: number;
  first_name?: string; 
  lastName?: string; 
  email?: string; 
  full_name?: string;
  license_status?: string;
}

export interface Patient {
  id: number;
  profile: number;
  first_name?: string; 
  lastName?: string; 
  email?: string; 
  full_name?: string;
}

export interface Appointment {
  id: number;
  doctor: number;
  patient: number;
  date_and_time: Date;
  doctor_full_name?: string;
  patient_full_name?: string;
  google_meet_link?: string;
}

export interface Service {
  id: number;
  name: string;
  specialty: number;
  specialty_name: string;
}

export interface Specialty {
  id: number;
  name: string;
}

export interface EventResponse {
  conferenceData?: {
    entryPoints?: {
      uri?: string;
    }[];
  };
}
