export const asyncSleep = async (timeMs: number): Promise<void> =>
  new Promise((resolve, reject) => {
    window.setTimeout(() => {
      resolve();
    }, timeMs);
  });
