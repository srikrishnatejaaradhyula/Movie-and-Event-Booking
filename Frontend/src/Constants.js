const production = {
    url: 'http://172.21.5.36:5000'
};

const development = {
    url: 'http://127.0.0.1:5000'
  };
// export const config = process.env.NODE_ENV === 'development' ? development : production;
export const config = development;
// export const config = production;