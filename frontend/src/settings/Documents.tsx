import { DocumentsProps } from '../models/misc';
import Trash from '../assets/trash.svg';

const Documents: React.FC<DocumentsProps> = ({
  documents,
  handleDeleteDocument,
}) => {
  return (
    <div className="mt-8">
      <div className="flex flex-col">
        <div className="mt-[27px] w-max overflow-x-auto rounded-xl border dark:border-chinese-silver">
          <table className="block w-full table-auto content-center justify-center text-center dark:text-bright-gray">
            <thead>
              <tr>
                <th className="border-r p-4 md:w-[244px]">Document Name</th>
                <th className="w-[244px] border-r px-4 py-2">Vector Date</th>
                <th className="w-[244px] border-r px-4 py-2">Type</th>
                <th className="px-4 py-2"></th>
              </tr>
            </thead>
            <tbody>
              {documents &&
                documents.map((document, index) => (
                  <tr key={index}>
                    <td className="border-r border-t px-4 py-2">
                      {document.name}
                    </td>
                    <td className="border-r border-t px-4 py-2">
                      {document.date}
                    </td>
                    <td className="border-r border-t px-4 py-2">
                      {document.location === 'remote'
                        ? 'Pre-loaded'
                        : 'Private'}
                    </td>
                    <td className="border-t px-4 py-2">
                      {document.location !== 'remote' && (
                        <img
                          src={Trash}
                          alt="Delete"
                          className="h-4 w-4 cursor-pointer hover:opacity-50"
                          id={`img-${index}`}
                          onClick={(event) => {
                            event.stopPropagation();
                            handleDeleteDocument(index, document);
                          }}
                        />
                      )}
                    </td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Documents;
