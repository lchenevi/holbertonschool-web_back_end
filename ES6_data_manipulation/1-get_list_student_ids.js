export default function getListStudentIds(value) {
  if (!Array.isArray(value)) {
    return [];
  }
  return value.map((element) => element.id);
}
